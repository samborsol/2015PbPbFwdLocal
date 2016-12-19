

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

ak4Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("ak4CaloJets"),
    matched = cms.InputTag("ak4GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.4
    )

ak4CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak4GenJets"),
    matched = cms.InputTag("ak4GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.4
    )

ak4Caloparton = patJetPartonMatch.clone(src = cms.InputTag("ak4CaloJets")
                                                        )

ak4Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("ak4CaloJets"),
    payload = "AK4Calo_offline"
    )

ak4CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('ak4CaloJets'))

#ak4Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak4GenJets'))

ak4CalobTagger = bTaggers("ak4Calo",0.4)

#create objects locally since they dont load properly otherwise
#ak4Calomatch = ak4CalobTagger.match
ak4Caloparton = patJetPartonMatch.clone(src = cms.InputTag("ak4CaloJets"), matched = cms.InputTag("genParticles"))
ak4CaloPatJetFlavourAssociationLegacy = ak4CalobTagger.PatJetFlavourAssociationLegacy
ak4CaloPatJetPartons = ak4CalobTagger.PatJetPartons
ak4CaloJetTracksAssociatorAtVertex = ak4CalobTagger.JetTracksAssociatorAtVertex
ak4CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
ak4CaloSimpleSecondaryVertexHighEffBJetTags = ak4CalobTagger.SimpleSecondaryVertexHighEffBJetTags
ak4CaloSimpleSecondaryVertexHighPurBJetTags = ak4CalobTagger.SimpleSecondaryVertexHighPurBJetTags
ak4CaloCombinedSecondaryVertexBJetTags = ak4CalobTagger.CombinedSecondaryVertexBJetTags
ak4CaloCombinedSecondaryVertexV2BJetTags = ak4CalobTagger.CombinedSecondaryVertexV2BJetTags
ak4CaloJetBProbabilityBJetTags = ak4CalobTagger.JetBProbabilityBJetTags
ak4CaloSoftPFMuonByPtBJetTags = ak4CalobTagger.SoftPFMuonByPtBJetTags
ak4CaloSoftPFMuonByIP3dBJetTags = ak4CalobTagger.SoftPFMuonByIP3dBJetTags
ak4CaloTrackCountingHighEffBJetTags = ak4CalobTagger.TrackCountingHighEffBJetTags
ak4CaloTrackCountingHighPurBJetTags = ak4CalobTagger.TrackCountingHighPurBJetTags
ak4CaloPatJetPartonAssociationLegacy = ak4CalobTagger.PatJetPartonAssociationLegacy

ak4CaloImpactParameterTagInfos = ak4CalobTagger.ImpactParameterTagInfos
ak4CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
ak4CaloJetProbabilityBJetTags = ak4CalobTagger.JetProbabilityBJetTags

ak4CaloSecondaryVertexTagInfos = ak4CalobTagger.SecondaryVertexTagInfos
ak4CaloSimpleSecondaryVertexHighEffBJetTags = ak4CalobTagger.SimpleSecondaryVertexHighEffBJetTags
ak4CaloSimpleSecondaryVertexHighPurBJetTags = ak4CalobTagger.SimpleSecondaryVertexHighPurBJetTags
ak4CaloCombinedSecondaryVertexBJetTags = ak4CalobTagger.CombinedSecondaryVertexBJetTags
ak4CaloCombinedSecondaryVertexV2BJetTags = ak4CalobTagger.CombinedSecondaryVertexV2BJetTags

ak4CaloSecondaryVertexNegativeTagInfos = ak4CalobTagger.SecondaryVertexNegativeTagInfos
ak4CaloNegativeSimpleSecondaryVertexHighEffBJetTags = ak4CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
ak4CaloNegativeSimpleSecondaryVertexHighPurBJetTags = ak4CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
ak4CaloNegativeCombinedSecondaryVertexBJetTags = ak4CalobTagger.NegativeCombinedSecondaryVertexBJetTags
ak4CaloPositiveCombinedSecondaryVertexBJetTags = ak4CalobTagger.PositiveCombinedSecondaryVertexBJetTags
ak4CaloNegativeCombinedSecondaryVertexV2BJetTags = ak4CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
ak4CaloPositiveCombinedSecondaryVertexV2BJetTags = ak4CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

ak4CaloSoftPFMuonsTagInfos = ak4CalobTagger.SoftPFMuonsTagInfos
ak4CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
ak4CaloSoftPFMuonBJetTags = ak4CalobTagger.SoftPFMuonBJetTags
ak4CaloSoftPFMuonByIP3dBJetTags = ak4CalobTagger.SoftPFMuonByIP3dBJetTags
ak4CaloSoftPFMuonByPtBJetTags = ak4CalobTagger.SoftPFMuonByPtBJetTags
ak4CaloNegativeSoftPFMuonByPtBJetTags = ak4CalobTagger.NegativeSoftPFMuonByPtBJetTags
ak4CaloPositiveSoftPFMuonByPtBJetTags = ak4CalobTagger.PositiveSoftPFMuonByPtBJetTags
ak4CaloPatJetFlavourIdLegacy = cms.Sequence(ak4CaloPatJetPartonAssociationLegacy*ak4CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#ak4CaloPatJetFlavourAssociation = ak4CalobTagger.PatJetFlavourAssociation
#ak4CaloPatJetFlavourId = cms.Sequence(ak4CaloPatJetPartons*ak4CaloPatJetFlavourAssociation)

ak4CaloJetBtaggingIP       = cms.Sequence(ak4CaloImpactParameterTagInfos *
            (ak4CaloTrackCountingHighEffBJetTags +
             ak4CaloTrackCountingHighPurBJetTags +
             ak4CaloJetProbabilityBJetTags +
             ak4CaloJetBProbabilityBJetTags 
            )
            )

ak4CaloJetBtaggingSV = cms.Sequence(ak4CaloImpactParameterTagInfos
            *
            ak4CaloSecondaryVertexTagInfos
            * (ak4CaloSimpleSecondaryVertexHighEffBJetTags+
                ak4CaloSimpleSecondaryVertexHighPurBJetTags+
                ak4CaloCombinedSecondaryVertexBJetTags+
                ak4CaloCombinedSecondaryVertexV2BJetTags
              )
            )

ak4CaloJetBtaggingNegSV = cms.Sequence(ak4CaloImpactParameterTagInfos
            *
            ak4CaloSecondaryVertexNegativeTagInfos
            * (ak4CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                ak4CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                ak4CaloNegativeCombinedSecondaryVertexBJetTags+
                ak4CaloPositiveCombinedSecondaryVertexBJetTags+
                ak4CaloNegativeCombinedSecondaryVertexV2BJetTags+
                ak4CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

ak4CaloJetBtaggingMu = cms.Sequence(ak4CaloSoftPFMuonsTagInfos * (ak4CaloSoftPFMuonBJetTags
                +
                ak4CaloSoftPFMuonByIP3dBJetTags
                +
                ak4CaloSoftPFMuonByPtBJetTags
                +
                ak4CaloNegativeSoftPFMuonByPtBJetTags
                +
                ak4CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

ak4CaloJetBtagging = cms.Sequence(ak4CaloJetBtaggingIP
            *ak4CaloJetBtaggingSV
            *ak4CaloJetBtaggingNegSV
#            *ak4CaloJetBtaggingMu
            )

ak4CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("ak4CaloJets"),
        genJetMatch          = cms.InputTag("ak4Calomatch"),
        genPartonMatch       = cms.InputTag("ak4Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak4Calocorr")),
        JetPartonMapSource   = cms.InputTag("ak4CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("ak4CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("ak4CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("ak4CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("ak4CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("ak4CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("ak4CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("ak4CaloJetBProbabilityBJetTags"),
            cms.InputTag("ak4CaloJetProbabilityBJetTags"),
            #cms.InputTag("ak4CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("ak4CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("ak4CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("ak4CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("ak4CaloJetID"),
        addBTagInfo = True,
        addTagInfos = True,
        addDiscriminators = True,
        addAssociatedTracks = True,
        addJetCharge = False,
        addJetID = False,
        getJetMCFlavour = False,
        addGenPartonMatch = False,
        addGenJetMatch = False,
        embedGenJetMatch = False,
        embedGenPartonMatch = False,
        # embedCaloTowers = False,
        # embedPFCandidates = True
        )

ak4CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("ak4CaloJets"),
           	    R0  = cms.double( 0.4)
)
ak4CalopatJetsWithBtagging.userData.userFloats.src += ['ak4CaloNjettiness:tau1','ak4CaloNjettiness:tau2','ak4CaloNjettiness:tau3']

ak4CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("ak4CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak4GenJets',
                                                             rParam = 0.4,
                                                             matchJets = cms.untracked.bool(False),
                                                             matchTag = 'patJetsWithBtagging',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("generalTracks"),
                                                             fillGenJets = False,
                                                             isMC = False,
							     doSubEvent = False,
                                                             useHepMC = cms.untracked.bool(False),
							     genParticles = cms.untracked.InputTag("genParticles"),
							     eventInfoTag = cms.InputTag("generator"),
                                                             doLifeTimeTagging = cms.untracked.bool(True),
                                                             doLifeTimeTaggingExtras = cms.untracked.bool(False),
                                                             bTagJetName = cms.untracked.string("ak4Calo"),
                                                             jetName = cms.untracked.string("ak4Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(False),
							     doSubJets = cms.untracked.bool(False),
                                                             doGenSubJets = cms.untracked.bool(False),     
                                                             subjetGenTag = cms.untracked.InputTag("ak4GenJets"),
                                                             doGenTaus = False
                                                             )

ak4CaloJetSequence_mc = cms.Sequence(
                                                  #ak4Caloclean
                                                  #*
                                                  ak4Calomatch
                                                  #*
                                                  #ak4CalomatchGroomed
                                                  *
                                                  ak4Caloparton
                                                  *
                                                  ak4Calocorr
                                                  *
                                                  #ak4CaloJetID
                                                  #*
                                                  ak4CaloPatJetFlavourIdLegacy
                                                  #*
			                          #ak4CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  ak4CaloJetTracksAssociatorAtVertex
                                                  *
                                                  ak4CaloJetBtagging
                                                  *
                                                  ak4CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  ak4CalopatJetsWithBtagging
                                                  *
                                                  ak4CaloJetAnalyzer
                                                  )

ak4CaloJetSequence_data = cms.Sequence(ak4Calocorr
                                                    *
                                                    #ak4CaloJetID
                                                    #*
                                                    ak4CaloJetTracksAssociatorAtVertex
                                                    *
                                                    ak4CaloJetBtagging
                                                    *
                                                    ak4CaloNjettiness 
                                                    *
                                                    ak4CalopatJetsWithBtagging
                                                    *
                                                    ak4CaloJetAnalyzer
                                                    )

ak4CaloJetSequence_jec = cms.Sequence(ak4CaloJetSequence_mc)
ak4CaloJetSequence_mb = cms.Sequence(ak4CaloJetSequence_mc)

ak4CaloJetSequence = cms.Sequence(ak4CaloJetSequence_data)
