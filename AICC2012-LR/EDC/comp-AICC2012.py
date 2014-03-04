import numpy as np
import matplotlib.pyplot as mpl
from scipy import interpolate

readarray=np.loadtxt('output.txt')

IC_depth=readarray[:,0]
IC_thinning=readarray[:,1]
IC_thinning_sigma=readarray[:,2]
IC_accu=readarray[:,3]
IC_accu_sigma=readarray[:,4]
IC_LID=readarray[:,5]
IC_LID_sigma=readarray[:,6]
IC_age=readarray[:,7]
IC_age_sigma=readarray[:,8]
IC_gage=readarray[:,9]
IC_gage_sigma=readarray[:,10]
IC_Ddepth=readarray[:,11]
IC_Ddepth_sigma=readarray[:,12]


readarray=np.loadtxt('AICC2012.txt')

AICC2012_depth=readarray[:,0]
AICC2012_age=readarray[:,1]
AICC2012_age_sigma=readarray[:,2]
AICC2012_gage=readarray[:,3]
AICC2012_gage_sigma=readarray[:,4]
AICC2012_accu=readarray[:,5]
AICC2012_thinning=readarray[:,6]
AICC2012_LID=readarray[:,7]/0.7

f=interpolate.interp1d(AICC2012_depth,AICC2012_age, bounds_error=False, fill_value=np.nan)
mpl.figure('Ice Age')
mpl.plot(IC_age-f(IC_depth),IC_depth)
mpl.show()
