

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVs2PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVs2PFJets"),
    matched = cms.InputTag("ak2HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.2
    )

akVs2PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak2HiGenJets"),
    matched = cms.InputTag("ak2HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.2
    )

akVs2PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVs2PFJets")
                                                        )

akVs2PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVs2PFJets"),
    payload = "AK2PF_offline"
    )

akVs2PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVs2CaloJets'))

#akVs2PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak2HiCleanedGenJets'))

akVs2PFbTagger = bTaggers("akVs2PF",0.2)

#create objects locally since they dont load properly otherwise
#akVs2PFmatch = akVs2PFbTagger.match
akVs2PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVs2PFJets"), matched = cms.InputTag("selectedPartons"))
akVs2PFPatJetFlavourAssociationLegacy = akVs2PFbTagger.PatJetFlavourAssociationLegacy
akVs2PFPatJetPartons = akVs2PFbTagger.PatJetPartons
akVs2PFJetTracksAssociatorAtVertex = akVs2PFbTagger.JetTracksAssociatorAtVertex
akVs2PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVs2PFSimpleSecondaryVertexHighEffBJetTags = akVs2PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVs2PFSimpleSecondaryVertexHighPurBJetTags = akVs2PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVs2PFCombinedSecondaryVertexBJetTags = akVs2PFbTagger.CombinedSecondaryVertexBJetTags
akVs2PFCombinedSecondaryVertexV2BJetTags = akVs2PFbTagger.CombinedSecondaryVertexV2BJetTags
akVs2PFJetBProbabilityBJetTags = akVs2PFbTagger.JetBProbabilityBJetTags
akVs2PFSoftPFMuonByPtBJetTags = akVs2PFbTagger.SoftPFMuonByPtBJetTags
akVs2PFSoftPFMuonByIP3dBJetTags = akVs2PFbTagger.SoftPFMuonByIP3dBJetTags
akVs2PFTrackCountingHighEffBJetTags = akVs2PFbTagger.TrackCountingHighEffBJetTags
akVs2PFTrackCountingHighPurBJetTags = akVs2PFbTagger.TrackCountingHighPurBJetTags
akVs2PFPatJetPartonAssociationLegacy = akVs2PFbTagger.PatJetPartonAssociationLegacy

akVs2PFImpactParameterTagInfos = akVs2PFbTagger.ImpactParameterTagInfos
akVs2PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVs2PFJetProbabilityBJetTags = akVs2PFbTagger.JetProbabilityBJetTags

akVs2PFSecondaryVertexTagInfos = akVs2PFbTagger.SecondaryVertexTagInfos
akVs2PFSimpleSecondaryVertexHighEffBJetTags = akVs2PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVs2PFSimpleSecondaryVertexHighPurBJetTags = akVs2PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVs2PFCombinedSecondaryVertexBJetTags = akVs2PFbTagger.CombinedSecondaryVertexBJetTags
akVs2PFCombinedSecondaryVertexV2BJetTags = akVs2PFbTagger.CombinedSecondaryVertexV2BJetTags

akVs2PFSecondaryVertexNegativeTagInfos = akVs2PFbTagger.SecondaryVertexNegativeTagInfos
akVs2PFNegativeSimpleSecondaryVertexHighEffBJetTags = akVs2PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVs2PFNegativeSimpleSecondaryVertexHighPurBJetTags = akVs2PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVs2PFNegativeCombinedSecondaryVertexBJetTags = akVs2PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akVs2PFPositiveCombinedSecondaryVertexBJetTags = akVs2PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akVs2PFNegativeCombinedSecondaryVertexV2BJetTags = akVs2PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVs2PFPositiveCombinedSecondaryVertexV2BJetTags = akVs2PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVs2PFSoftPFMuonsTagInfos = akVs2PFbTagger.SoftPFMuonsTagInfos
akVs2PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVs2PFSoftPFMuonBJetTags = akVs2PFbTagger.SoftPFMuonBJetTags
akVs2PFSoftPFMuonByIP3dBJetTags = akVs2PFbTagger.SoftPFMuonByIP3dBJetTags
akVs2PFSoftPFMuonByPtBJetTags = akVs2PFbTagger.SoftPFMuonByPtBJetTags
akVs2PFNegativeSoftPFMuonByPtBJetTags = akVs2PFbTagger.NegativeSoftPFMuonByPtBJetTags
akVs2PFPositiveSoftPFMuonByPtBJetTags = akVs2PFbTagger.PositiveSoftPFMuonByPtBJetTags
akVs2PFPatJetFlavourIdLegacy = cms.Sequence(akVs2PFPatJetPartonAssociationLegacy*akVs2PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVs2PFPatJetFlavourAssociation = akVs2PFbTagger.PatJetFlavourAssociation
#akVs2PFPatJetFlavourId = cms.Sequence(akVs2PFPatJetPartons*akVs2PFPatJetFlavourAssociation)

akVs2PFJetBtaggingIP       = cms.Sequence(akVs2PFImpactParameterTagInfos *
            (akVs2PFTrackCountingHighEffBJetTags +
             akVs2PFTrackCountingHighPurBJetTags +
             akVs2PFJetProbabilityBJetTags +
             akVs2PFJetBProbabilityBJetTags 
            )
            )

akVs2PFJetBtaggingSV = cms.Sequence(akVs2PFImpactParameterTagInfos
            *
            akVs2PFSecondaryVertexTagInfos
            * (akVs2PFSimpleSecondaryVertexHighEffBJetTags+
                akVs2PFSimpleSecondaryVertexHighPurBJetTags+
                akVs2PFCombinedSecondaryVertexBJetTags+
                akVs2PFCombinedSecondaryVertexV2BJetTags
              )
            )

akVs2PFJetBtaggingNegSV = cms.Sequence(akVs2PFImpactParameterTagInfos
            *
            akVs2PFSecondaryVertexNegativeTagInfos
            * (akVs2PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVs2PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVs2PFNegativeCombinedSecondaryVertexBJetTags+
                akVs2PFPositiveCombinedSecondaryVertexBJetTags+
                akVs2PFNegativeCombinedSecondaryVertexV2BJetTags+
                akVs2PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVs2PFJetBtaggingMu = cms.Sequence(akVs2PFSoftPFMuonsTagInfos * (akVs2PFSoftPFMuonBJetTags
                +
                akVs2PFSoftPFMuonByIP3dBJetTags
                +
                akVs2PFSoftPFMuonByPtBJetTags
                +
                akVs2PFNegativeSoftPFMuonByPtBJetTags
                +
                akVs2PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akVs2PFJetBtagging = cms.Sequence(akVs2PFJetBtaggingIP
            *akVs2PFJetBtaggingSV
            *akVs2PFJetBtaggingNegSV
#            *akVs2PFJetBtaggingMu
            )

akVs2PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVs2PFJets"),
        genJetMatch          = cms.InputTag("akVs2PFmatch"),
        genPartonMatch       = cms.InputTag("akVs2PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs2PFcorr")),
        JetPartonMapSource   = cms.InputTag("akVs2PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVs2PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVs2PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVs2PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVs2PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVs2PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVs2PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVs2PFJetBProbabilityBJetTags"),
            cms.InputTag("akVs2PFJetProbabilityBJetTags"),
            #cms.InputTag("akVs2PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVs2PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVs2PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akVs2PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVs2PFJetID"),
        addBTagInfo = True,
        addTagInfos = True,
        addDiscriminators = True,
        addAssociatedTracks = True,
        addJetCharge = False,
        addJetID = False,
        getJetMCFlavour = True,
        addGenPartonMatch = True,
        addGenJetMatch = True,
        embedGenJetMatch = True,
        embedGenPartonMatch = True,
        # embedCaloTowers = False,
        # embedPFCandidates = True
        )

akVs2PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVs2PFJets"),
           	    R0  = cms.double( 0.2)
)
akVs2PFpatJetsWithBtagging.userData.userFloats.src += ['akVs2PFNjettiness:tau1','akVs2PFNjettiness:tau2','akVs2PFNjettiness:tau3']

akVs2PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVs2PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak2HiGenJets',
                                                             rParam = 0.2,
                                                             matchJets = cms.untracked.bool(False),
                                                             matchTag = 'patJetsWithBtagging',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("hiGeneralTracks"),
                                                             fillGenJets = True,
                                                             isMC = True,
							     doSubEvent = True,
                                                             useHepMC = cms.untracked.bool(False),
							     genParticles = cms.untracked.InputTag("genParticles"),
							     eventInfoTag = cms.InputTag("generator"),
                                                             doLifeTimeTagging = cms.untracked.bool(True),
                                                             doLifeTimeTaggingExtras = cms.untracked.bool(False),
                                                             bTagJetName = cms.untracked.string("akVs2PF"),
                                                             jetName = cms.untracked.string("akVs2PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
							     doSubJets = cms.untracked.bool(False),
                                                             doGenSubJets = cms.untracked.bool(False),     
                                                             subjetGenTag = cms.untracked.InputTag("ak2GenJets"),
                                                             doGenTaus = True
                                                             )

akVs2PFJetSequence_mc = cms.Sequence(
                                                  #akVs2PFclean
                                                  #*
                                                  akVs2PFmatch
                                                  #*
                                                  #akVs2PFmatchGroomed
                                                  *
                                                  akVs2PFparton
                                                  *
                                                  akVs2PFcorr
                                                  *
                                                  #akVs2PFJetID
                                                  #*
                                                  akVs2PFPatJetFlavourIdLegacy
                                                  #*
			                          #akVs2PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVs2PFJetTracksAssociatorAtVertex
                                                  *
                                                  akVs2PFJetBtagging
                                                  *
                                                  akVs2PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVs2PFpatJetsWithBtagging
                                                  *
                                                  akVs2PFJetAnalyzer
                                                  )

akVs2PFJetSequence_data = cms.Sequence(akVs2PFcorr
                                                    *
                                                    #akVs2PFJetID
                                                    #*
                                                    akVs2PFJetTracksAssociatorAtVertex
                                                    *
                                                    akVs2PFJetBtagging
                                                    *
                                                    akVs2PFNjettiness 
                                                    *
                                                    akVs2PFpatJetsWithBtagging
                                                    *
                                                    akVs2PFJetAnalyzer
                                                    )

akVs2PFJetSequence_jec = cms.Sequence(akVs2PFJetSequence_mc)
akVs2PFJetSequence_mb = cms.Sequence(akVs2PFJetSequence_mc)

akVs2PFJetSequence = cms.Sequence(akVs2PFJetSequence_mb)
