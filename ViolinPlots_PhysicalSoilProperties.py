'''
  //////////////////////////////////////////////////////////////////////////////////////////	
/Kevin Achieng																				/
/03/27/2019																					/
/University of Wyoming, Civil & Architectural Engineering Department						/
/Violin-plots and Scatter plots of ObservedAWC vs Observeds predictedd Soil with one RCM omitted 	/
  //////////////////////////////////////////////////////////////////////////////////////////	
'''
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import seaborn as sns
from scipy import stats
from pylab import text 

# Fix a random seed  to initialize random no. generator
# initialized random number generator to ensure that the results are REPRODUCIBLE
np.random.seed(111)
#Globally set figure parameters by using a rcParams dictionary:
params = {'legend.fontsize': 12,
         'figure.figsize': (10, 10),
         'axes.labelsize': 12,
         'axes.titlesize':12,
		 'axes.labelweight': 'bold',
         'xtick.labelsize':12,
         'ytick.labelsize':12}
pylab.rcParams.update(params)

# A) Calibrated
SoilData1 = pd.read_csv('E:/ViolinPlots/AWC_Region1_5000_Data.csv', index_col=None)
SoilData1 = SoilData1.dropna()
SoilData1 = SoilData1.convert_objects(convert_numeric=True)
SoilData2 = pd.read_csv('E:/ViolinPlots/AWC_Region2_6000_Data.csv', index_col=None)
SoilData2 = SoilData2.dropna()
SoilData2 = SoilData2.convert_objects(convert_numeric=True)
SoilData3 = pd.read_csv('E:/ViolinPlots/AWC_Region3_7000_Data.csv', index_col=None)
SoilData3 = SoilData3.dropna()
SoilData3 = SoilData3.convert_objects(convert_numeric=True)
SoilData4 = pd.read_csv('E:/ViolinPlots/AWC_Region4_1000_Data.csv', index_col=None)
SoilData4 = SoilData4.dropna()
SoilData4 = SoilData4.convert_objects(convert_numeric=True)
SoilData5 = pd.read_csv('E:/ViolinPlots/AWC_Region5_2000_Data.csv', index_col=None)
SoilData5 = SoilData5.dropna()
SoilData5 = SoilData5.convert_objects(convert_numeric=True)
SoilData6 = pd.read_csv('E:/ViolinPlots/AWC_Region6_9000_Data.csv', index_col=None)
SoilData6 = SoilData6.dropna()
SoilData6 = SoilData6.convert_objects(convert_numeric=True)

SoilData_ALL = pd.read_csv('E:/ViolinPlots/AWC_Region1_to_6.csv', index_col=None)
SoilData_ALL = SoilData_ALL.dropna()
SoilData_ALL = SoilData_ALL.convert_objects(convert_numeric=True)


#cols = SoilData1.columns 
#SoilData1 = SoilData1.astype(float)
print(SoilData1.dtypes)
print(SoilData_ALL.dtypes)
#SoilData1 = pd.to_numeric(SoilData1)
#SoilData1 = SoilData1.astype(np.float64)
y_mean1 = SoilData1['AWC_cm.per.cm.'].mean()
print(y_mean1)

#Set Color palettes.
#print('*'*10 + ' Set Color palettes in plots ' + '*'*10)
# pkmn_type_colors = ['#78C850',  # Grass
                    # '#F08030',  # Fire
                    # '#6890F0',  # Water
                    # '#A8B820',  # Bug
                    # '#A8A878',  # Normal
                    # '#A040A0',  # Poison
                    # '#F8D030',  # Electric
                    # '#E0C068',  # Ground
                    # '#EE99AC',  # Fairy
                    # '#C03028',  # Fighting
                    # '#F85888',  # Psychic
                    # '#B8A038',  # Rock
                    # #'#705898',  # Ghost
                    # #'#98D8D8',  # Ice
                    # #'#7038F8',  # Dragon
                   # ]
#pylab.rcParams['font.family'] = ['Times New Roman']


params = {'legend.fontsize': 12,
		'figure.figsize': (10,13),
		'axes.labelsize': 12,
		'axes.titlesize':11,
		'axes.labelweight': 'bold',
		'axes.titleweight': 'bold',
		'xtick.labelsize':12,
		'ytick.labelsize':12}
pylab.rcParams.update(params)
#sns.set_style("dark") #Set background color
#plot violinplots
print('*'*10 + ' plot Calibrated Percent Change violinplots ' + '*'*10)
fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(nrows=3, ncols=2,  sharex=False, sharey=False)
#Set the violinplot linewidth
sns.set_context(rc = {'patch.linewidth': 1.0, 'edgecolor': 'black'})
#ax1
sns.violinplot(x="Regions", y="AWC_cm.per.cm.",  data=SoilData_ALL, ci=95, capsize=.2, saturation=.5,  ax=ax1)
ax1.set(xlabel='', ylabel='AWC (cm/cm)')
ax1.set_title('(a)')
# mu = SoilData_ALL["AWC_cm.per.cm."].mean()
# median = np.median(SoilData_ALL["AWC_cm.per.cm."])
# sigma = SoilData_ALL["AWC_cm.per.cm."].std()
# textstr = '$\mu=%.2f$\n$\mathrm{median}=%.2f$\n$\sigma=%.2f$'%(mu, median, sigma)
# # these are matplotlib.patch.Patch properties
# props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
# # place a text box in upper left in axes coords
# ax1.text(0.05, 0.95, textstr, transform=ax1.transAxes, fontsize=12, verticalalignment='center', bbox=props)
ax1.tick_params(labelbottom=False)  
#ax1.legend(loc='upper right',ncol=1)
#ax1.get_legend().remove()
#plt.xticks(rotation=45, ha='right')

#ax2 
sns.violinplot(x="Regions", y="Sand_Percent",  data=SoilData_ALL, ci=95, capsize=.2, saturation=.5,  ax=ax2)
ax2.set(xlabel='', ylabel='Sand (%)')
ax2.set_title('(b)')
ax2.tick_params(labelbottom=False)  
#ax2.legend(loc='upper right',ncol=1)
#ax2.get_legend().remove()

#ax3
sns.violinplot(x="Regions", y="Silt_Percent",  data=SoilData_ALL, ci=95, capsize=.2, saturation=.5,  ax=ax3)
ax3.set(xlabel=' ', ylabel='Silt (%)')
ax3.set_title('(c)')
ax3.tick_params(labelbottom=False)  

#ax4
sns.violinplot(x="Regions", y="Clay_Percent",  data=SoilData_ALL, ci=95, capsize=.2, saturation=.5,  ax=ax4)
ax4.set_title('(d)')
ax4.set(xlabel='', ylabel='Clay (%)')
ax4.tick_params(labelbottom=False)
# ax4.set_xticklabels(ax4.get_xticklabels(), rotation=45, ha="right")
#ax4.get_legend().remove()

#ax5
sns.violinplot(x="Regions", y="Moist.BD_g.per.cm3.",  data=SoilData_ALL, ci=95, capsize=.2, saturation=.5,  ax=ax5)
ax5.set(xlabel='Regions', ylabel='Bulk Density ($g/cm^3$)')
ax5.set_title('(e)')
ax5.tick_params(labelbottom=True)

#ax6
sns.violinplot(x="Regions", y="OM_Percent",  data=SoilData_ALL, ci=95, capsize=.2, saturation=.5,  ax=ax6)
ax6.set(xlabel='Regions', ylabel='OM (%)')
ax6.set_title('(f)')
ax6.set_ylim(0, 20)
ax6.yaxis.set_ticks(np.arange(0, 21, 5))
ax6.tick_params(labelbottom=True)

#plt.xticks(rotation=45, ha='right')
plt.savefig('./Figure/' + 'PhysicalSoilProperties'+'_ViolinPlots'+'.png', bbox_inches="tight", dpi=600)
plt.savefig('./Figure/' + 'PhysicalSoilProperties'+'_ViolinPlots'+'.pdf', bbox_inches="tight", dpi=600)
plt.savefig('./Figure/' + 'PhysicalSoilProperties'+'_ViolinPlots'+'.eps', bbox_inches="tight", dpi=600)
plt.show()

