//
// $Id: AdditionalEventInfo.cc,v 1.1 2015/08/23 13:49:16 battilan Exp $
//

/**
  \class    AdditionalEventInfo 
  \brief    Adds bx, orbit and inst lumi info (the last from scalers)
            
  \Author   Carlo Battilana
  \version  $Id: AdditionalEventInfo.cc,v 1.1 2015/01/06 10:41:10 battilan Exp $
*/


#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"


#include "DataFormats/Scalers/interface/LumiScalers.h"
#include "DataFormats/Luminosity/interface/LumiDetails.h"

#include "DataFormats/Candidate/interface/CompositeCandidate.h"
#include "DataFormats/Common/interface/ValueMap.h"




class AdditionalEventInfo : public edm::EDProducer
{
  
public:

  explicit AdditionalEventInfo(const edm::ParameterSet & iConfig);
  virtual ~AdditionalEventInfo() { }

  virtual void produce(edm::Event & iEvent, const edm::EventSetup & iSetup) final;

private:

  edm::InputTag m_lumiScalerTag;
  edm::InputTag m_pairTag;

  /// Write a ValueMap<T> in the event
  template<typename T> void writeValueMap(edm::Event &ev, const edm::Handle<edm::View<reco::Candidate> > & handle,
					  const std::vector<T> & values, const std::string    & label) const ;

};


AdditionalEventInfo::AdditionalEventInfo(const edm::ParameterSet & iConfig) :
  m_lumiScalerTag(iConfig.getParameter<edm::InputTag>("lumiScalerTag")),
  m_pairTag(iConfig.getParameter<edm::InputTag>("pairTag"))
{
  
  produces<edm::ValueMap<float> >("bxId");
  // produces<edm::ValueMap<ULong64_t> >("orbit");
  produces<edm::ValueMap<float> >("instLumi");

}

void AdditionalEventInfo::produce(edm::Event & ev, const edm::EventSetup & iSetup)
{

  float bxId  = -999;
  // ULong64_t orbit = 0;

  float instLumi = -999.;

  if (ev.isRealData())
    {
      bxId  = ev.bunchCrossing();
      // orbit = ev.orbitNumber();

      if (m_lumiScalerTag.label() != "none")
	{
	  edm::Handle<LumiScalersCollection> lumiScaler;
	  ev.getByLabel(m_lumiScalerTag, lumiScaler);

	  if (lumiScaler->begin() != lumiScaler->end())
	    instLumi= lumiScaler->begin()->instantLumi();
	} 
    } 

  edm::Handle<edm::View<reco::Candidate> > pairs;
  ev.getByLabel(m_pairTag, pairs);

  size_t n = pairs->size();
  
  std::vector<float> bxIds(n,0.);
  // std::vector<ULong64_t> orbits(n,0);
  std::vector<float> instLumis(n,0.);
  
  for (size_t iPair = 0; iPair < n; ++iPair)
    {
      const reco::Candidate & pair = (*pairs)[iPair];
      if (pair.numberOfDaughters() != 2) throw cms::Exception("CorruptData") << 
					   "[AdditionalEventInfo::produce] AdditionalEventInfo should be used on composite candidates with two daughters, this one has " << pair.numberOfDaughters() << "\n";
      
      bxIds[iPair]     = bxId;
      //orbits[iPair]    = orbit;
      instLumis[iPair] = instLumi;
    }

  writeValueMap<float>(ev, pairs, bxIds, "bxId");
  // writeValueMap<ULong64_t>(ev, pairs, orbits, "orbit");
  writeValueMap<float>(ev, pairs, instLumis, "instLumi");

}

template<typename T> void AdditionalEventInfo::writeValueMap(edm::Event & ev, const edm::Handle<edm::View<reco::Candidate> > & handle,
							     const std::vector<T> & values, const std::string & label) const 
{
  
  std::auto_ptr<edm::ValueMap<T> > valMap(new edm::ValueMap<T>());
  typename edm::ValueMap<T>::Filler filler(*valMap);
  filler.insert(handle, values.begin(), values.end());
  filler.fill();
  ev.put(valMap, label);
  
}


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(AdditionalEventInfo);
