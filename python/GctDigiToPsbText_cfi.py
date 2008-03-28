import FWCore.ParameterSet.Config as cms

gctDigiToPsbText = cms.EDFilter("GctDigiToPsbText",
    GctInputLabel = cms.InputTag("gtPsbTextToDigi"),
    TextFileName = cms.string('psb-out-'),
    HexUpperCase = cms.untracked.bool(False)
)


