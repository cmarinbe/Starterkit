
## Basic DV job with GaudiExec
j = Job('First ganga job')
myApp = prepareGaudiExec('DaVinci','v41r2')
myApp.options = ['code/davinci-grid/ntuple_options_grid.py']
myApp.readInputData('data/MC_2012_27163003_Beam4000GeV2012MagDownNu2.5Pythia8_Sim08e_Digi13_Trig0x409f0045_Reco14a_Stripping20NoPrescalingFlagged_ALLSTREAMS.DST.py')
j.application = myApp
j.backend = Dirac()
j.submit()

# send output to eos
#f = MassStorageFile('DVntuple.root')
#f.outputfilenameformat = '/starterkit/{jid}_{fname}'
#j.outputfiles = [f]

# submit
#j.submit()
