#ifndef MNguyen_HiInclusiveJetAnalyzer_inclusiveJetAnalyzer_
#define MNguyen_HiInclusiveJetAnalyzer_inclusiveJetAnalyzer_

// system include files
#include <memory>
#include <string>
#include <iostream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "TFile.h"
#include "TTree.h"
#include "TH1.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "Geometry/CaloGeometry/interface/CaloGeometry.h"

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutSetup.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerObjectMapRecord.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerObjectMap.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

#include "fastjet/contrib/Njettiness.hh"
#include "TMVA/Reader.h"
//

/**\class HiInclusiveJetAnalyzer

   \author Matt Nguyen
   \date   November 2010
*/




class HiInclusiveJetAnalyzer : public edm::EDAnalyzer {
public:

  explicit HiInclusiveJetAnalyzer(const edm::ParameterSet&);

  ~HiInclusiveJetAnalyzer();

  virtual void analyze(const edm::Event&, const edm::EventSetup&);

  virtual void beginRun(const edm::Run & r, const edm::EventSetup & c);

  virtual void beginJob();

  void fillL1Bits(const edm::Event &iEvent);

  void fillHLTBits(const edm::Event &iEvent);

  template <typename TYPE>
    void getProduct(const std::string name, edm::Handle<TYPE> &prod,
		    const edm::Event &event) const;
  template <typename TYPE>
    bool getProductSafe(const std::string name, edm::Handle<TYPE> &prod,
			const edm::Event &event) const;


private:

  int getPFJetMuon(const pat::Jet& pfJet, const reco::PFCandidateCollection *pfCandidateColl);

  double getPtRel(const reco::PFCandidate lep, const pat::Jet& jet );

  void saveDaughters( const reco::GenParticle & gen);
  void saveDaughters( const reco::Candidate & gen);
  double getEt(math::XYZPoint pos, double energy);
  math::XYZPoint getPosition(const DetId &id, reco::Vertex::Point vtx = reco::Vertex::Point(0,0,0));
  int TaggedJet(reco::Jet calojet, edm::Handle<reco::JetTagCollection > jetTags );
  float getTau(unsigned num, const reco::GenJet object) const;
  void analyzeSubjets(const reco::Jet jet);
  int  getGroomedGenJetIndex(const reco::GenJet jet) const;
  void analyzeRefSubjets(const reco::GenJet jet);
  void analyzeGenSubjets(const reco::GenJet jet);
  float getAboveCharmThresh(reco::TrackRefVector& selTracks, const reco::TrackIPTagInfo& ipData, int sigOrVal);
 
  std::auto_ptr<fastjet::contrib::Njettiness>   routine_;
  
  // edm::InputTag   jetTag_, vtxTag_, genjetTag_, eventInfoTag_, L1gtReadout_, pfCandidateLabel_, trackTag_, matchTag_;
  edm::InputTag   jetTagLabel_;
  edm::EDGetTokenT<std::vector<reco::Vertex> >         vtxTag_;
  edm::EDGetTokenT<reco::JetView>              jetTag_;
  edm::EDGetTokenT<pat::JetCollection>         jetTagPat_;
  edm::EDGetTokenT<reco::JetView>              matchTag_;
  edm::EDGetTokenT<pat::JetCollection>         matchTagPat_;
  edm::EDGetTokenT<reco::JetView>              subjetGenTag_;
  edm::EDGetTokenT<reco::PFCandidateCollection>         pfCandidateLabel_;
  edm::EDGetTokenT<reco::TrackCollection>         trackTag_;
  edm::EDGetTokenT<reco::GenParticleCollection>         genParticleSrc_;
  edm::EDGetTokenT<std::vector<reco::GenJet> >         genjetTag_;
  //edm::EDGetTokenT<edm::View<reco::Jet>>         genjetTag_;
  edm::EDGetTokenT<edm::HepMCProduct>         eventInfoTag_;
  edm::EDGetTokenT<GenEventInfoProduct>  eventGenInfoTag_;
  edm::EDGetTokenT< L1GlobalTriggerReadoutRecord >         L1gtReadout_;
  // edm::InputTag HcalRecHitHFSrc_;
  // edm::InputTag HcalRecHitHBHESrc_;
  // edm::InputTag EBSrc_;
  // edm::InputTag EESrc_;
  // edm::InputTag genParticleSrc_;

  std::string jetName_; //used as prefix for jet structures
  edm::Handle<reco::JetView> gensubjets_;
  /* edm::EDGetTokenT< edm::ValueMap<float> > tokenGenTau1_; */
  /* edm::EDGetTokenT< edm::ValueMap<float> > tokenGenTau2_; */
  /* edm::EDGetTokenT< edm::ValueMap<float> > tokenGenTau3_; */
  
  // towers
  edm::EDGetTokenT<CaloTowerCollection> TowerSrc_;

  std::vector<float> usedStringPts;

  //for the JetID BDT
  std::unique_ptr<TMVA::Reader> reader;
  std::unique_ptr<float[]> varAddr;

  /// verbose ?
  bool verbose_;
  bool doMatch_;
  bool useVtx_;
  bool useJEC_;
  bool usePat_;
  bool doTower;
  bool isMC_;
  bool useHepMC_;
  bool fillGenJets_;
  bool doTrigger_;
  bool useQuality_;
  std::string trackQuality_;

  bool doSubEvent_;
  double genPtMin_;
  bool doLifeTimeTagging_;
  bool doLifeTimeTaggingExtras_;
  bool saveBfragments_;
  bool skipCorrections_;
  bool doExtraCTagging_;

  bool doHiJetID_;
  bool doStandardJetID_;

  double rParam;
  double hardPtMin_;
  double jetPtMin_;
  bool doGenTaus_;
  bool doSubJets_;
  bool doGenSubJets_;

  TTree *t;
  edm::Service<TFileService> fs1;

  const CaloGeometry *geo;

  edm::EDGetTokenT<edm::TriggerResults> hltResName_;         //HLT trigger results name
  std::vector<std::string>      hltProcNames_;       //HLT process name(s)
  std::vector<std::string>      hltTrgNames_;        //HLT trigger name(s)

  std::vector<int>              hltTrgBits_;         //HLT trigger bit(s)
  std::vector<bool>             hltTrgDeci_;         //HLT trigger descision(s)
  std::vector<std::string>      hltTrgUsedNames_;    //HLT used trigger name(s)
  std::string                   hltUsedResName_;     //used HLT trigger results name
  std::string			jetIDweightFile_;

  std::string bTagJetName_;
  edm::EDGetTokenT<std::vector<reco::TrackIPTagInfo> > ImpactParameterTagInfos_;
  edm::EDGetTokenT<reco::JetTagCollection> TrackCountingHighEffBJetTags_;
  edm::EDGetTokenT<reco::JetTagCollection> TrackCountingHighPurBJetTags_;
  edm::EDGetTokenT<reco::JetTagCollection> JetProbabilityBJetTags_;
  edm::EDGetTokenT<reco::JetTagCollection> JetBProbabilityBJetTags_;
  edm::EDGetTokenT<std::vector<reco::SecondaryVertexTagInfo> > SecondaryVertexTagInfos_;
  edm::EDGetTokenT<std::vector<reco::SecondaryVertexTagInfo> > SecondaryVertexNegativeTagInfos_;
  edm::EDGetTokenT<reco::JetTagCollection> SimpleSecondaryVertexHighEffBJetTags_;
  edm::EDGetTokenT<reco::JetTagCollection> NegativeSimpleSecondaryVertexHighEffBJetTags_;
  edm::EDGetTokenT<reco::JetTagCollection> SimpleSecondaryVertexHighPurBJetTags_;
  edm::EDGetTokenT<reco::JetTagCollection> NegativeSimpleSecondaryVertexHighPurBJetTags_;
  edm::EDGetTokenT<reco::JetTagCollection> CombinedSecondaryVertexBJetTags_;
  edm::EDGetTokenT<reco::JetTagCollection> NegativeCombinedSecondaryVertexBJetTags_;
  edm::EDGetTokenT<reco::JetTagCollection> PositiveCombinedSecondaryVertexBJetTags_;
  edm::EDGetTokenT<reco::JetTagCollection> CombinedSecondaryVertexV2BJetTags_;
  edm::EDGetTokenT<reco::JetTagCollection> NegativeCombinedSecondaryVertexV2BJetTags_;
  edm::EDGetTokenT<reco::JetTagCollection> PositiveCombinedSecondaryVertexV2BJetTags_;
  edm::EDGetTokenT<reco::JetTagCollection> NegativeSoftPFMuonByPtBJetTags_;
  edm::EDGetTokenT<reco::JetTagCollection> PositiveSoftPFMuonByPtBJetTags_;

  static const int MAXJETS = 500;
  static const int MAXTRACKS = 5000;
  static const int MAXHLTBITS = 5000;
  static const int MAXBFRAG = 500;

  struct JRA{

    int nref;
    int run;
    int evt;
    int lumi;
    int bin;
    float vx, vy, vz;
    float b;
    float hf;

    float rawpt[MAXJETS];
    float jtpt[MAXJETS];
    float jteta[MAXJETS];
    float jtphi[MAXJETS];
    float jty[MAXJETS];
    float jtpu[MAXJETS];
    float jtm[MAXJETS];
    float jtarea[MAXJETS];

    float jtPfCHF[MAXJETS];
    float jtPfNHF[MAXJETS];
    float jtPfCEF[MAXJETS];
    float jtPfNEF[MAXJETS];
    float jtPfMUF[MAXJETS];

    int jtPfCHM[MAXJETS];
    int jtPfNHM[MAXJETS];
    int jtPfCEM[MAXJETS];
    int jtPfNEM[MAXJETS];
    int jtPfMUM[MAXJETS];
    
    float jttau1[MAXJETS];
    float jttau2[MAXJETS];
    float jttau3[MAXJETS];

    std::vector<std::vector<float>> jtSubJetPt;
    std::vector<std::vector<float>> jtSubJetEta;
    std::vector<std::vector<float>> jtSubJetPhi;
    std::vector<std::vector<float>> jtSubJetM;
    
    float trackMax[MAXJETS];
    float trackSum[MAXJETS];
    int trackN[MAXJETS];

    float chargedMax[MAXJETS];
    float chargedSum[MAXJETS];
    int chargedN[MAXJETS];

    float photonMax[MAXJETS];
    float photonSum[MAXJETS];
    int photonN[MAXJETS];

    float trackHardSum[MAXJETS];
    float chargedHardSum[MAXJETS];
    float photonHardSum[MAXJETS];

    int trackHardN[MAXJETS];
    int chargedHardN[MAXJETS];
    int photonHardN[MAXJETS];

    float neutralMax[MAXJETS];
    float neutralSum[MAXJETS];
    int neutralN[MAXJETS];

    float eMax[MAXJETS];
    float eSum[MAXJETS];
    int eN[MAXJETS];

    float muMax[MAXJETS];
    float muSum[MAXJETS];
    int muN[MAXJETS];

    float genChargedSum[MAXJETS];
    float genHardSum[MAXJETS];
    float signalChargedSum[MAXJETS];
    float signalHardSum[MAXJETS];

    // Update by Raghav, modified to take it from the towers
    float hcalSum[MAXJETS];
    float ecalSum[MAXJETS];


    float fHPD[MAXJETS];
    float fRBX[MAXJETS];
    int n90[MAXJETS];
    float fSubDet1[MAXJETS];
    float fSubDet2[MAXJETS];
    float fSubDet3[MAXJETS];
    float fSubDet4[MAXJETS];
    float restrictedEMF[MAXJETS];
    int nHCAL[MAXJETS];
    int nECAL[MAXJETS];
    float apprHPD[MAXJETS];
    float apprRBX[MAXJETS];

    //    int n90[MAXJETS];
    int n2RPC[MAXJETS];
    int n3RPC[MAXJETS];
    int nRPC[MAXJETS];

    float fEB[MAXJETS];
    float fEE[MAXJETS];
    float fHB[MAXJETS];
    float fHE[MAXJETS];
    float fHO[MAXJETS];
    float fLong[MAXJETS];
    float fShort[MAXJETS];
    float fLS[MAXJETS];
    float fHFOOT[MAXJETS];


    int subid[MAXJETS];

    float matchedPt[MAXJETS];
    float matchedRawPt[MAXJETS];
    float matchedR[MAXJETS];
    float matchedPu[MAXJETS];

    float discr_csvV1[MAXJETS];
    float discr_csvV2[MAXJETS];
    float discr_muByIp3[MAXJETS];
    float discr_muByPt[MAXJETS];
    float discr_prob[MAXJETS];
    float discr_probb[MAXJETS];
    float discr_tcHighEff[MAXJETS];
    float discr_tcHighPur[MAXJETS];
    float discr_ssvHighEff[MAXJETS];
    float discr_ssvHighPur[MAXJETS];

    float ndiscr_ssvHighEff[MAXJETS];
    float ndiscr_ssvHighPur[MAXJETS];
    float ndiscr_csvV1[MAXJETS];
    float ndiscr_csvV2[MAXJETS];
    float ndiscr_muByPt[MAXJETS];

    float pdiscr_csvV1[MAXJETS];
    float pdiscr_csvV2[MAXJETS];

    int nsvtx[MAXJETS];
    int svtxntrk[MAXJETS];
    float svtxdl[MAXJETS];
    float svtxdls[MAXJETS];
    float svtxdl2d[MAXJETS];
    float svtxdls2d[MAXJETS];
    float svtxm[MAXJETS];
    float svtxpt[MAXJETS];
    float svtxmcorr[MAXJETS];
    float svtxnormchi2[MAXJETS];
    float svJetDeltaR[MAXJETS];
    float svtxTrkSumChi2[MAXJETS];
    int svtxTrkNetCharge[MAXJETS];
    int svtxNtrkInCone[MAXJETS];

    int nIPtrk[MAXJETS];
    int nselIPtrk[MAXJETS];

    int nIP;
    int ipJetIndex[MAXTRACKS];
    float ipPt[MAXTRACKS];
    float ipEta[MAXTRACKS];
    float ipDxy[MAXTRACKS];
    float ipDz[MAXTRACKS];
    float ipChi2[MAXTRACKS];
    int ipNHit[MAXTRACKS];
    int ipNHitPixel[MAXTRACKS];
    int ipNHitStrip[MAXTRACKS];
    bool ipIsHitL1[MAXTRACKS];
    float ipProb0[MAXTRACKS];
    float ipProb1[MAXTRACKS];
    float ip2d[MAXTRACKS];
    float ip2dSig[MAXTRACKS];
    float ip3d[MAXTRACKS];
    float ip3dSig[MAXTRACKS];
    float ipDist2Jet[MAXTRACKS];
    float ipDist2JetSig[MAXTRACKS];
    float ipClosest2Jet[MAXTRACKS];
  
    float trackPtRel[MAXTRACKS];
    float trackPtRatio[MAXTRACKS];
    float trackPPar[MAXTRACKS];
    float trackPParRatio[MAXTRACKS];
    float trackDeltaR[MAXTRACKS];

    float trackSip2dSigAboveCharm[MAXJETS];
    float trackSip2dValAboveCharm[MAXJETS];
    float trackSip3dValAboveCharm[MAXJETS];
    float trackSip3dSigAboveCharm[MAXJETS];
    float trackSumJetDeltaR[MAXJETS];

    float mue[MAXJETS];
    float mupt[MAXJETS];
    float mueta[MAXJETS];
    float muphi[MAXJETS];
    float mudr[MAXJETS];
    float muptrel[MAXJETS];
    int muchg[MAXJETS];

    float discr_fr01[MAXJETS];
    float discr_jetID_cuts[MAXJETS];
    float discr_jetID_bdt[MAXJETS];

    float refpt[MAXJETS];
    float refeta[MAXJETS];
    float refphi[MAXJETS];
    float refm[MAXJETS];
    float refarea[MAXJETS];
    float refy[MAXJETS];
    float reftau1[MAXJETS];
    float reftau2[MAXJETS];
    float reftau3[MAXJETS];
    float refdphijt[MAXJETS];
    float refdrjt[MAXJETS];
    float refparton_pt[MAXJETS];
    int refparton_flavor[MAXJETS];
    int refparton_flavorForB[MAXJETS];

    float refptG[MAXJETS];
    float refetaG[MAXJETS];
    float refphiG[MAXJETS];
    float refmG[MAXJETS];
    std::vector<std::vector<float>> refSubJetPt;
    std::vector<std::vector<float>> refSubJetEta;
    std::vector<std::vector<float>> refSubJetPhi;
    std::vector<std::vector<float>> refSubJetM;
    

    float pthat;
    int beamId1, beamId2;
    int ngen;
    int genmatchindex[MAXJETS];
    float genpt[MAXJETS];
    float geneta[MAXJETS];
    float genphi[MAXJETS];
    float genm[MAXJETS];
    float geny[MAXJETS];
    float gentau1[MAXJETS];
    float gentau2[MAXJETS];
    float gentau3[MAXJETS];
    float gendphijt[MAXJETS];
    float gendrjt[MAXJETS];
    int gensubid[MAXJETS];

    float genptG[MAXJETS];
    float genetaG[MAXJETS];
    float genphiG[MAXJETS];
    float genmG[MAXJETS];
    std::vector<std::vector<float>> genSubJetPt;
    std::vector<std::vector<float>> genSubJetEta;
    std::vector<std::vector<float>> genSubJetPhi;
    std::vector<std::vector<float>> genSubJetM;
    std::vector<std::vector<float>> genSubJetArea;
    
    // hlt
    int nHLTBit;
    bool hltBit[MAXHLTBITS];

    // l1
    int nL1TBit;
    bool l1TBit[MAXHLTBITS];
    int nL1ABit;
    bool l1ABit[MAXHLTBITS];

    int bMult;
    int bJetIndex[MAXBFRAG];
    int bStatus[MAXBFRAG];
    int bPdg[MAXBFRAG];
    int bChg[MAXBFRAG];
    float bVx[MAXBFRAG];
    float bVy[MAXBFRAG];
    float bVz[MAXBFRAG];
    float bPt[MAXBFRAG];
    float bEta[MAXBFRAG];
    float bPhi[MAXBFRAG];


  };

  JRA jets_;

};

#endif
