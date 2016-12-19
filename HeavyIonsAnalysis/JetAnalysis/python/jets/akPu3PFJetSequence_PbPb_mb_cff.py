

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPu3PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu3PFJets"),
    matched = cms.InputTag("ak3HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.3
    )

akPu3PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak3HiGenJets"),
    matched = cms.InputTag("ak3HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.3
    )

akPu3PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPu3PFJets")
                                                        )

akPu3PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akPu3PFJets"),
    payload = "AKPu3PF_offline"
    )

akPu3PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akPu3CaloJets'))

#akPu3PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak3HiCleanedGenJets'))

akPu3PFbTagger = bTaggers("akPu3PF",0.3)

#create objects locally since they dont load properly otherwise
#akPu3PFmatch = akPu3PFbTagger.match
akPu3PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPu3PFJets"), matched = cms.InputTag("selectedPartons"))
akPu3PFPatJetFlavourAssociationLegacy = akPu3PFbTagger.PatJetFlavourAssociationLegacy
akPu3PFPatJetPartons = akPu3PFbTagger.PatJetPartons
akPu3PFJetTracksAssociatorAtVertex = akPu3PFbTagger.JetTracksAssociatorAtVertex
akPu3PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPu3PFSimpleSecondaryVertexHighEffBJetTags = akPu3PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPu3PFSimpleSecondaryVertexHighPurBJetTags = akPu3PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPu3PFCombinedSecondaryVertexBJetTags = akPu3PFbTagger.CombinedSecondaryVertexBJetTags
akPu3PFCombinedSecondaryVertexV2BJetTags = akPu3PFbTagger.CombinedSecondaryVertexV2BJetTags
akPu3PFJetBProbabilityBJetTags = akPu3PFbTagger.JetBProbabilityBJetTags
akPu3PFSoftPFMuonByPtBJetTags = akPu3PFbTagger.SoftPFMuonByPtBJetTags
akPu3PFSoftPFMuonByIP3dBJetTags = akPu3PFbTagger.SoftPFMuonByIP3dBJetTags
akPu3PFTrackCountingHighEffBJetTags = akPu3PFbTagger.TrackCountingHighEffBJetTags
akPu3PFTrackCountingHighPurBJetTags = akPu3PFbTagger.TrackCountingHighPurBJetTags
akPu3PFPatJetPartonAssociationLegacy = akPu3PFbTagger.PatJetPartonAssociationLegacy

akPu3PFImpactParameterTagInfos = akPu3PFbTagger.ImpactParameterTagInfos
akPu3PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu3PFJetProbabilityBJetTags = akPu3PFbTagger.JetProbabilityBJetTags

akPu3PFSecondaryVertexTagInfos = akPu3PFbTagger.SecondaryVertexTagInfos
akPu3PFSimpleSecondaryVertexHighEffBJetTags = akPu3PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPu3PFSimpleSecondaryVertexHighPurBJetTags = akPu3PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPu3PFCombinedSecondaryVertexBJetTags = akPu3PFbTagger.CombinedSecondaryVertexBJetTags
akPu3PFCombinedSecondaryVertexV2BJetTags = akPu3PFbTagger.CombinedSecondaryVertexV2BJetTags

akPu3PFSecondaryVertexNegativeTagInfos = akPu3PFbTagger.SecondaryVertexNegativeTagInfos
akPu3PFNegativeSimpleSecondaryVertexHighEffBJetTags = akPu3PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPu3PFNegativeSimpleSecondaryVertexHighPurBJetTags = akPu3PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPu3PFNegativeCombinedSecondaryVertexBJetTags = akPu3PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akPu3PFPositiveCombinedSecondaryVertexBJetTags = akPu3PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akPu3PFNegativeCombinedSecondaryVertexV2BJetTags = akPu3PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPu3PFPositiveCombinedSecondaryVertexV2BJetTags = akPu3PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPu3PFSoftPFMuonsTagInfos = akPu3PFbTagger.SoftPFMuonsTagInfos
akPu3PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu3PFSoftPFMuonBJetTags = akPu3PFbTagger.SoftPFMuonBJetTags
akPu3PFSoftPFMuonByIP3dBJetTags = akPu3PFbTagger.SoftPFMuonByIP3dBJetTags
akPu3PFSoftPFMuonByPtBJetTags = akPu3PFbTagger.SoftPFMuonByPtBJetTags
akPu3PFNegativeSoftPFMuonByPtBJetTags = akPu3PFbTagger.NegativeSoftPFMuonByPtBJetTags
akPu3PFPositiveSoftPFMuonByPtBJetTags = akPu3PFbTagger.PositiveSoftPFMuonByPtBJetTags
akPu3PFPatJetFlavourIdLegacy = cms.Sequence(akPu3PFPatJetPartonAssociationLegacy*akPu3PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akPu3PFPatJetFlavourAssociation = akPu3PFbTagger.PatJetFlavourAssociation
#akPu3PFPatJetFlavourId = cms.Sequence(akPu3PFPatJetPartons*akPu3PFPatJetFlavourAssociation)

akPu3PFJetBtaggingIP       = cms.Sequence(akPu3PFImpactParameterTagInfos *
            (akPu3PFTrackCountingHighEffBJetTags +
             akPu3PFTrackCountingHighPurBJetTags +
             akPu3PFJetProbabilityBJetTags +
             akPu3PFJetBProbabilityBJetTags 
            )
            )

akPu3PFJetBtaggingSV = cms.Sequence(akPu3PFImpactParameterTagInfos
            *
            akPu3PFSecondaryVertexTagInfos
            * (akPu3PFSimpleSecondaryVertexHighEffBJetTags+
                akPu3PFSimpleSecondaryVertexHighPurBJetTags+
                akPu3PFCombinedSecondaryVertexBJetTags+
                akPu3PFCombinedSecondaryVertexV2BJetTags
              )
            )

akPu3PFJetBtaggingNegSV = cms.Sequence(akPu3PFImpactParameterTagInfos
            *
            akPu3PFSecondaryVertexNegativeTagInfos
            * (akPu3PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akPu3PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akPu3PFNegativeCombinedSecondaryVertexBJetTags+
                akPu3PFPositiveCombinedSecondaryVertexBJetTags+
                akPu3PFNegativeCombinedSecondaryVertexV2BJetTags+
                akPu3PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akPu3PFJetBtaggingMu = cms.Sequence(akPu3PFSoftPFMuonsTagInfos * (akPu3PFSoftPFMuonBJetTags
                +
                akPu3PFSoftPFMuonByIP3dBJetTags
                +
                akPu3PFSoftPFMuonByPtBJetTags
                +
                akPu3PFNegativeSoftPFMuonByPtBJetTags
                +
                akPu3PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akPu3PFJetBtagging = cms.Sequence(akPu3PFJetBtaggingIP
            *akPu3PFJetBtaggingSV
            *akPu3PFJetBtaggingNegSV
#            *akPu3PFJetBtaggingMu
            )

akPu3PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akPu3PFJets"),
        genJetMatch          = cms.InputTag("akPu3PFmatch"),
        genPartonMatch       = cms.InputTag("akPu3PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3PFcorr")),
        JetPartonMapSource   = cms.InputTag("akPu3PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akPu3PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPu3PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akPu3PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPu3PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPu3PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPu3PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akPu3PFJetBProbabilityBJetTags"),
            cms.InputTag("akPu3PFJetProbabilityBJetTags"),
            #cms.InputTag("akPu3PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akPu3PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akPu3PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akPu3PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPu3PFJetID"),
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

akPu3PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akPu3PFJets"),
           	    R0  = cms.double( 0.3)
)
akPu3PFpatJetsWithBtagging.userData.userFloats.src += ['akPu3PFNjettiness:tau1','akPu3PFNjettiness:tau2','akPu3PFNjettiness:tau3']

akPu3PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu3PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak3HiGenJets',
                                                             rParam = 0.3,
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
                                                             bTagJetName = cms.untracked.string("akPu3PF"),
                                                             jetName = cms.untracked.string("akPu3PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
							     doSubJets = cms.untracked.bool(False),
                                                             doGenSubJets = cms.untracked.bool(False),     
                                                             subjetGenTag = cms.untracked.InputTag("ak3GenJets"),
                                                             doGenTaus = True
                                                             )

akPu3PFJetSequence_mc = cms.Sequence(
                                                  #akPu3PFclean
                                                  #*
                                                  akPu3PFmatch
                                                  #*
                                                  #akPu3PFmatchGroomed
                                                  *
                                                  akPu3PFparton
                                                  *
                                                  akPu3PFcorr
                                                  *
                                                  #akPu3PFJetID
                                                  #*
                                                  akPu3PFPatJetFlavourIdLegacy
                                                  #*
			                          #akPu3PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akPu3PFJetTracksAssociatorAtVertex
                                                  *
                                                  akPu3PFJetBtagging
                                                  *
                                                  akPu3PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akPu3PFpatJetsWithBtagging
                                                  *
                                                  akPu3PFJetAnalyzer
                                                  )

akPu3PFJetSequence_data = cms.Sequence(akPu3PFcorr
                                                    *
                                                    #akPu3PFJetID
                                                    #*
                                                    akPu3PFJetTracksAssociatorAtVertex
                                                    *
                                                    akPu3PFJetBtagging
                                                    *
                                                    akPu3PFNjettiness 
                                                    *
                                                    akPu3PFpatJetsWithBtagging
                                                    *
                                                    akPu3PFJetAnalyzer
                                                    )

akPu3PFJetSequence_jec = cms.Sequence(akPu3PFJetSequence_mc)
akPu3PFJetSequence_mb = cms.Sequence(akPu3PFJetSequence_mc)

akPu3PFJetSequence = cms.Sequence(akPu3PFJetSequence_mb)
