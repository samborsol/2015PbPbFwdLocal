

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPu6Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu6CaloJets"),
    matched = cms.InputTag("ak6HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.6
    )

akPu6CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak6HiGenJets"),
    matched = cms.InputTag("ak6HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.6
    )

akPu6Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPu6CaloJets")
                                                        )

akPu6Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akPu6CaloJets"),
    payload = "AKPu6Calo_offline"
    )

akPu6CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akPu6CaloJets'))

#akPu6Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak6HiSignalGenJets'))

akPu6CalobTagger = bTaggers("akPu6Calo",0.6)

#create objects locally since they dont load properly otherwise
#akPu6Calomatch = akPu6CalobTagger.match
akPu6Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPu6CaloJets"), matched = cms.InputTag("hiSignalGenParticles"))
akPu6CaloPatJetFlavourAssociationLegacy = akPu6CalobTagger.PatJetFlavourAssociationLegacy
akPu6CaloPatJetPartons = akPu6CalobTagger.PatJetPartons
akPu6CaloJetTracksAssociatorAtVertex = akPu6CalobTagger.JetTracksAssociatorAtVertex
akPu6CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPu6CaloSimpleSecondaryVertexHighEffBJetTags = akPu6CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPu6CaloSimpleSecondaryVertexHighPurBJetTags = akPu6CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPu6CaloCombinedSecondaryVertexBJetTags = akPu6CalobTagger.CombinedSecondaryVertexBJetTags
akPu6CaloCombinedSecondaryVertexV2BJetTags = akPu6CalobTagger.CombinedSecondaryVertexV2BJetTags
akPu6CaloJetBProbabilityBJetTags = akPu6CalobTagger.JetBProbabilityBJetTags
akPu6CaloSoftPFMuonByPtBJetTags = akPu6CalobTagger.SoftPFMuonByPtBJetTags
akPu6CaloSoftPFMuonByIP3dBJetTags = akPu6CalobTagger.SoftPFMuonByIP3dBJetTags
akPu6CaloTrackCountingHighEffBJetTags = akPu6CalobTagger.TrackCountingHighEffBJetTags
akPu6CaloTrackCountingHighPurBJetTags = akPu6CalobTagger.TrackCountingHighPurBJetTags
akPu6CaloPatJetPartonAssociationLegacy = akPu6CalobTagger.PatJetPartonAssociationLegacy

akPu6CaloImpactParameterTagInfos = akPu6CalobTagger.ImpactParameterTagInfos
akPu6CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu6CaloJetProbabilityBJetTags = akPu6CalobTagger.JetProbabilityBJetTags

akPu6CaloSecondaryVertexTagInfos = akPu6CalobTagger.SecondaryVertexTagInfos
akPu6CaloSimpleSecondaryVertexHighEffBJetTags = akPu6CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPu6CaloSimpleSecondaryVertexHighPurBJetTags = akPu6CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPu6CaloCombinedSecondaryVertexBJetTags = akPu6CalobTagger.CombinedSecondaryVertexBJetTags
akPu6CaloCombinedSecondaryVertexV2BJetTags = akPu6CalobTagger.CombinedSecondaryVertexV2BJetTags

akPu6CaloSecondaryVertexNegativeTagInfos = akPu6CalobTagger.SecondaryVertexNegativeTagInfos
akPu6CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akPu6CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPu6CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akPu6CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPu6CaloNegativeCombinedSecondaryVertexBJetTags = akPu6CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akPu6CaloPositiveCombinedSecondaryVertexBJetTags = akPu6CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akPu6CaloNegativeCombinedSecondaryVertexV2BJetTags = akPu6CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPu6CaloPositiveCombinedSecondaryVertexV2BJetTags = akPu6CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPu6CaloSoftPFMuonsTagInfos = akPu6CalobTagger.SoftPFMuonsTagInfos
akPu6CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu6CaloSoftPFMuonBJetTags = akPu6CalobTagger.SoftPFMuonBJetTags
akPu6CaloSoftPFMuonByIP3dBJetTags = akPu6CalobTagger.SoftPFMuonByIP3dBJetTags
akPu6CaloSoftPFMuonByPtBJetTags = akPu6CalobTagger.SoftPFMuonByPtBJetTags
akPu6CaloNegativeSoftPFMuonByPtBJetTags = akPu6CalobTagger.NegativeSoftPFMuonByPtBJetTags
akPu6CaloPositiveSoftPFMuonByPtBJetTags = akPu6CalobTagger.PositiveSoftPFMuonByPtBJetTags
akPu6CaloPatJetFlavourIdLegacy = cms.Sequence(akPu6CaloPatJetPartonAssociationLegacy*akPu6CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akPu6CaloPatJetFlavourAssociation = akPu6CalobTagger.PatJetFlavourAssociation
#akPu6CaloPatJetFlavourId = cms.Sequence(akPu6CaloPatJetPartons*akPu6CaloPatJetFlavourAssociation)

akPu6CaloJetBtaggingIP       = cms.Sequence(akPu6CaloImpactParameterTagInfos *
            (akPu6CaloTrackCountingHighEffBJetTags +
             akPu6CaloTrackCountingHighPurBJetTags +
             akPu6CaloJetProbabilityBJetTags +
             akPu6CaloJetBProbabilityBJetTags 
            )
            )

akPu6CaloJetBtaggingSV = cms.Sequence(akPu6CaloImpactParameterTagInfos
            *
            akPu6CaloSecondaryVertexTagInfos
            * (akPu6CaloSimpleSecondaryVertexHighEffBJetTags+
                akPu6CaloSimpleSecondaryVertexHighPurBJetTags+
                akPu6CaloCombinedSecondaryVertexBJetTags+
                akPu6CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akPu6CaloJetBtaggingNegSV = cms.Sequence(akPu6CaloImpactParameterTagInfos
            *
            akPu6CaloSecondaryVertexNegativeTagInfos
            * (akPu6CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akPu6CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akPu6CaloNegativeCombinedSecondaryVertexBJetTags+
                akPu6CaloPositiveCombinedSecondaryVertexBJetTags+
                akPu6CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akPu6CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akPu6CaloJetBtaggingMu = cms.Sequence(akPu6CaloSoftPFMuonsTagInfos * (akPu6CaloSoftPFMuonBJetTags
                +
                akPu6CaloSoftPFMuonByIP3dBJetTags
                +
                akPu6CaloSoftPFMuonByPtBJetTags
                +
                akPu6CaloNegativeSoftPFMuonByPtBJetTags
                +
                akPu6CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akPu6CaloJetBtagging = cms.Sequence(akPu6CaloJetBtaggingIP
            *akPu6CaloJetBtaggingSV
            *akPu6CaloJetBtaggingNegSV
#            *akPu6CaloJetBtaggingMu
            )

akPu6CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akPu6CaloJets"),
        genJetMatch          = cms.InputTag("akPu6Calomatch"),
        genPartonMatch       = cms.InputTag("akPu6Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu6Calocorr")),
        JetPartonMapSource   = cms.InputTag("akPu6CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akPu6CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPu6CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akPu6CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPu6CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPu6CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPu6CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akPu6CaloJetBProbabilityBJetTags"),
            cms.InputTag("akPu6CaloJetProbabilityBJetTags"),
            #cms.InputTag("akPu6CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akPu6CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akPu6CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akPu6CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPu6CaloJetID"),
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

akPu6CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akPu6CaloJets"),
           	    R0  = cms.double( 0.6)
)
akPu6CalopatJetsWithBtagging.userData.userFloats.src += ['akPu6CaloNjettiness:tau1','akPu6CaloNjettiness:tau2','akPu6CaloNjettiness:tau3']

akPu6CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu6CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak6HiGenJets',
                                                             rParam = 0.6,
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
                                                             bTagJetName = cms.untracked.string("akPu6Calo"),
                                                             jetName = cms.untracked.string("akPu6Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
							     doSubJets = cms.untracked.bool(False),
                                                             doGenSubJets = cms.untracked.bool(False),     
                                                             subjetGenTag = cms.untracked.InputTag("ak6GenJets"),
                                                             doGenTaus = True
                                                             )

akPu6CaloJetSequence_mc = cms.Sequence(
                                                  #akPu6Caloclean
                                                  #*
                                                  akPu6Calomatch
                                                  #*
                                                  #akPu6CalomatchGroomed
                                                  *
                                                  akPu6Caloparton
                                                  *
                                                  akPu6Calocorr
                                                  *
                                                  #akPu6CaloJetID
                                                  #*
                                                  akPu6CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akPu6CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akPu6CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akPu6CaloJetBtagging
                                                  *
                                                  akPu6CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akPu6CalopatJetsWithBtagging
                                                  *
                                                  akPu6CaloJetAnalyzer
                                                  )

akPu6CaloJetSequence_data = cms.Sequence(akPu6Calocorr
                                                    *
                                                    #akPu6CaloJetID
                                                    #*
                                                    akPu6CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akPu6CaloJetBtagging
                                                    *
                                                    akPu6CaloNjettiness 
                                                    *
                                                    akPu6CalopatJetsWithBtagging
                                                    *
                                                    akPu6CaloJetAnalyzer
                                                    )

akPu6CaloJetSequence_jec = cms.Sequence(akPu6CaloJetSequence_mc)
akPu6CaloJetSequence_mb = cms.Sequence(akPu6CaloJetSequence_mc)

akPu6CaloJetSequence = cms.Sequence(akPu6CaloJetSequence_mc)
