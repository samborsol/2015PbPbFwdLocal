import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_data_cfi import *
hiEvtAnalyzer.doMC          = cms.bool(True)
hiEvtAnalyzer.doHiMC          = cms.bool(False)
hiEvtAnalyzer.useHepMC      = cms.bool(False)
