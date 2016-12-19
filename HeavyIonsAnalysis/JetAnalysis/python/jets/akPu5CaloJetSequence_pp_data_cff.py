

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPu5Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu5CaloJets"),
    matched = cms.InputTag("ak5GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.5
    )

akPu5CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak5GenJets"),
    matched = cms.InputTag("ak5GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.5
    )

akPu5Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPu5CaloJets")
                                                        )

akPu5Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akPu5CaloJets"),
    payload = "AKPu5Calo_offline"
    )

akPu5CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akPu5CaloJets'))

#akPu5Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak5GenJets'))

akPu5CalobTagger = bTaggers("akPu5Calo",0.5)

#create objects locally since they dont load properly otherwise
#akPu5Calomatch = akPu5CalobTagger.match
akPu5Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPu5CaloJets"), matched = cms.InputTag("genParticles"))
akPu5CaloPatJetFlavourAssociationLegacy = akPu5CalobTagger.PatJetFlavourAssociationLegacy
akPu5CaloPatJetPartons = akPu5CalobTagger.PatJetPartons
akPu5CaloJetTracksAssociatorAtVertex = akPu5CalobTagger.JetTracksAssociatorAtVertex
akPu5CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPu5CaloSimpleSecondaryVertexHighEffBJetTags = akPu5CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPu5CaloSimpleSecondaryVertexHighPurBJetTags = akPu5CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPu5CaloCombinedSecondaryVertexBJetTags = akPu5CalobTagger.CombinedSecondaryVertexBJetTags
akPu5CaloCombinedSecondaryVertexV2BJetTags = akPu5CalobTagger.CombinedSecondaryVertexV2BJetTags
akPu5CaloJetBProbabilityBJetTags = akPu5CalobTagger.JetBProbabilityBJetTags
akPu5CaloSoftPFMuonByPtBJetTags = akPu5CalobTagger.SoftPFMuonByPtBJetTags
akPu5CaloSoftPFMuonByIP3dBJetTags = akPu5CalobTagger.SoftPFMuonByIP3dBJetTags
akPu5CaloTrackCountingHighEffBJetTags = akPu5CalobTagger.TrackCountingHighEffBJetTags
akPu5CaloTrackCountingHighPurBJetTags = akPu5CalobTagger.TrackCountingHighPurBJetTags
akPu5CaloPatJetPartonAssociationLegacy = akPu5CalobTagger.PatJetPartonAssociationLegacy

akPu5CaloImpactParameterTagInfos = akPu5CalobTagger.ImpactParameterTagInfos
akPu5CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu5CaloJetProbabilityBJetTags = akPu5CalobTagger.JetProbabilityBJetTags

akPu5CaloSecondaryVertexTagInfos = akPu5CalobTagger.SecondaryVertexTagInfos
akPu5CaloSimpleSecondaryVertexHighEffBJetTags = akPu5CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPu5CaloSimpleSecondaryVertexHighPurBJetTags = akPu5CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPu5CaloCombinedSecondaryVertexBJetTags = akPu5CalobTagger.CombinedSecondaryVertexBJetTags
akPu5CaloCombinedSecondaryVertexV2BJetTags = akPu5CalobTagger.CombinedSecondaryVertexV2BJetTags

akPu5CaloSecondaryVertexNegativeTagInfos = akPu5CalobTagger.SecondaryVertexNegativeTagInfos
akPu5CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akPu5CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPu5CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akPu5CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPu5CaloNegativeCombinedSecondaryVertexBJetTags = akPu5CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akPu5CaloPositiveCombinedSecondaryVertexBJetTags = akPu5CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akPu5CaloNegativeCombinedSecondaryVertexV2BJetTags = akPu5CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPu5CaloPositiveCombinedSecondaryVertexV2BJetTags = akPu5CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPu5CaloSoftPFMuonsTagInfos = akPu5CalobTagger.SoftPFMuonsTagInfos
akPu5CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu5CaloSoftPFMuonBJetTags = akPu5CalobTagger.SoftPFMuonBJetTags
akPu5CaloSoftPFMuonByIP3dBJetTags = akPu5CalobTagger.SoftPFMuonByIP3dBJetTags
akPu5CaloSoftPFMuonByPtBJetTags = akPu5CalobTagger.SoftPFMuonByPtBJetTags
akPu5CaloNegativeSoftPFMuonByPtBJetTags = akPu5CalobTagger.NegativeSoftPFMuonByPtBJetTags
akPu5CaloPositiveSoftPFMuonByPtBJetTags = akPu5CalobTagger.PositiveSoftPFMuonByPtBJetTags
akPu5CaloPatJetFlavourIdLegacy = cms.Sequence(akPu5CaloPatJetPartonAssociationLegacy*akPu5CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akPu5CaloPatJetFlavourAssociation = akPu5CalobTagger.PatJetFlavourAssociation
#akPu5CaloPatJetFlavourId = cms.Sequence(akPu5CaloPatJetPartons*akPu5CaloPatJetFlavourAssociation)

akPu5CaloJetBtaggingIP       = cms.Sequence(akPu5CaloImpactParameterTagInfos *
            (akPu5CaloTrackCountingHighEffBJetTags +
             akPu5CaloTrackCountingHighPurBJetTags +
             akPu5CaloJetProbabilityBJetTags +
             akPu5CaloJetBProbabilityBJetTags 
            )
            )

akPu5CaloJetBtaggingSV = cms.Sequence(akPu5CaloImpactParameterTagInfos
            *
            akPu5CaloSecondaryVertexTagInfos
            * (akPu5CaloSimpleSecondaryVertexHighEffBJetTags+
                akPu5CaloSimpleSecondaryVertexHighPurBJetTags+
                akPu5CaloCombinedSecondaryVertexBJetTags+
                akPu5CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akPu5CaloJetBtaggingNegSV = cms.Sequence(akPu5CaloImpactParameterTagInfos
            *
            akPu5CaloSecondaryVertexNegativeTagInfos
            * (akPu5CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akPu5CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akPu5CaloNegativeCombinedSecondaryVertexBJetTags+
                akPu5CaloPositiveCombinedSecondaryVertexBJetTags+
                akPu5CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akPu5CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akPu5CaloJetBtaggingMu = cms.Sequence(akPu5CaloSoftPFMuonsTagInfos * (akPu5CaloSoftPFMuonBJetTags
                +
                akPu5CaloSoftPFMuonByIP3dBJetTags
                +
                akPu5CaloSoftPFMuonByPtBJetTags
                +
                akPu5CaloNegativeSoftPFMuonByPtBJetTags
                +
                akPu5CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akPu5CaloJetBtagging = cms.Sequence(akPu5CaloJetBtaggingIP
            *akPu5CaloJetBtaggingSV
            *akPu5CaloJetBtaggingNegSV
#            *akPu5CaloJetBtaggingMu
            )

akPu5CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akPu5CaloJets"),
        genJetMatch          = cms.InputTag("akPu5Calomatch"),
        genPartonMatch       = cms.InputTag("akPu5Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu5Calocorr")),
        JetPartonMapSource   = cms.InputTag("akPu5CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akPu5CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPu5CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akPu5CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPu5CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPu5CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPu5CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akPu5CaloJetBProbabilityBJetTags"),
            cms.InputTag("akPu5CaloJetProbabilityBJetTags"),
            #cms.InputTag("akPu5CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akPu5CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akPu5CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akPu5CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPu5CaloJetID"),
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

akPu5CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akPu5CaloJets"),
           	    R0  = cms.double( 0.5)
)
akPu5CalopatJetsWithBtagging.userData.userFloats.src += ['akPu5CaloNjettiness:tau1','akPu5CaloNjettiness:tau2','akPu5CaloNjettiness:tau3']

akPu5CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu5CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak5GenJets',
                                                             rParam = 0.5,
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
                                                             bTagJetName = cms.untracked.string("akPu5Calo"),
                                                             jetName = cms.untracked.string("akPu5Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(False),
							     doSubJets = cms.untracked.bool(False),
                                                             doGenSubJets = cms.untracked.bool(False),     
                                                             subjetGenTag = cms.untracked.InputTag("ak5GenJets"),
                                                             doGenTaus = False
                                                             )

akPu5CaloJetSequence_mc = cms.Sequence(
                                                  #akPu5Caloclean
                                                  #*
                                                  akPu5Calomatch
                                                  #*
                                                  #akPu5CalomatchGroomed
                                                  *
                                                  akPu5Caloparton
                                                  *
                                                  akPu5Calocorr
                                                  *
                                                  #akPu5CaloJetID
                                                  #*
                                                  akPu5CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akPu5CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akPu5CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akPu5CaloJetBtagging
                                                  *
                                                  akPu5CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akPu5CalopatJetsWithBtagging
                                                  *
                                                  akPu5CaloJetAnalyzer
                                                  )

akPu5CaloJetSequence_data = cms.Sequence(akPu5Calocorr
                                                    *
                                                    #akPu5CaloJetID
                                                    #*
                                                    akPu5CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akPu5CaloJetBtagging
                                                    *
                                                    akPu5CaloNjettiness 
                                                    *
                                                    akPu5CalopatJetsWithBtagging
                                                    *
                                                    akPu5CaloJetAnalyzer
                                                    )

akPu5CaloJetSequence_jec = cms.Sequence(akPu5CaloJetSequence_mc)
akPu5CaloJetSequence_mb = cms.Sequence(akPu5CaloJetSequence_mc)

akPu5CaloJetSequence = cms.Sequence(akPu5CaloJetSequence_data)
