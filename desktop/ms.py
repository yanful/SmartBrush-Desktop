import cv2
import numpy as np
import matplotlib.pyplot as plt

# Transformation matrix
WM = np.array([
    [0.0511018776280859,	0.121913014224580,	0.00381789269893684],
    [0.0330796467798949,	0.0726480154705813,	0.0192383898521178],
    [0.0274401161931692,	0.0753009475440036,	0.0606647914351527],
    [0.0303816608044601, 0.111699489095222, 0.132781004747960], 
    [0.0373910954529801,	0.155856741695505,	0.249672590007287],
    [0.0519181111982816,	0.199582059783363,	0.319638232721702],
    [0.0503179475996278,	0.191822928915983,	0.315414751285518],
    [0.0450945858036761,	0.183133367863638,	0.291951943420610],
    [0.0404969133621304,	0.192979200677526,	0.279272181164968],
    [0.0271209791016850,	0.196435747801436,	0.240671245295555],
    [-0.00152921331154664,	0.275295882053527,	0.196231854218493],
    [-0.0292786808444440,	0.420016296913875,	0.112978872158334],
    [-0.0387398585183248,	0.462125036694536,	0.0193976531475318],
    [-0.0397886176316223,	0.411344548229085,	-0.0156346798809241],
    [-0.0303621897024141,	0.327316873204226,	-0.0239130525884565],
    [-0.0170890486049735,	0.269360684119264,	-0.0255515333260028],
    [-0.00907261964601315,	0.249147701096224,	-0.0262411922799872],
    [0.00696118454471982,	0.195338655696655,	-0.0157473307180473],
    [0.0375915570493416,	0.147792978610750,	-0.0125562019961060],
    [0.0968311977538705,	0.143380973095655,	-0.0135932013153839],
    [0.190713030985450,	0.144874388861524,	-0.0118307359045622],
    [0.255095204445855,	0.129894596927978,	-0.00715847954245218],
    [0.240656674887936,	0.105758082124347,	-0.00436698167614128],
    [0.193896959810246,	0.0871169244046745,	-0.00246315897502304],
    [0.155329933158897,	0.0733667446559594,	-0.00105722927103152],
    [0.119715617327801,	0.0563609120011723,	-0.000959901827252788],
    [0.0957800434526012,	0.0461592234652808,	-0.000734845840842284],
    [0.0784396444257696,	0.0404226024987563,	-0.000587691434601744],
    [0.0558148635522882,	0.0324280248829314,	0.000723862860880863],
    [0.0368832241177084,	0.0269308504930881,	0.000888929808738496],
    [0.0271072492931279,	0.0239108670867227,	0.000446074471807744]
])

# Image read
Sample_read = cv2.imread('s (1).jpg')
Sample_read = cv2.cvtColor(Sample_read, cv2.COLOR_BGR2RGB)
Sample_read_gray = cv2.cvtColor(Sample_read, cv2.COLOR_RGB2GRAY)

# Displaying RGB image
plt.figure(figsize=(5, 5))  # Set appropriate figure size
plt.imshow(Sample_read_gray, cmap='gray', vmin=0, vmax=100)
plt.colorbar()
plt.axis('off')
plt.tight_layout()
plt.show()

al, aw, ch = Sample_read.shape
lrgb = Sample_read.reshape((al*aw, ch)).T
recoimage = WM.dot(lrgb)
recvol = recoimage.reshape((31, al, aw))
reco = np.transpose(recvol, (1, 2, 0))

# Displaying multispectral image
for j in range(31):
    plt.figure()
    plt.imshow(reco[:, :, j], cmap='gray', vmin=0, vmax=100)
    plt.colorbar()
    plt.axis('off')
    plt.tight_layout()
    picname = f'msi/s (1)_({400+10*(j)} nm).jpg'
    plt.savefig(picname, bbox_inches='tight')

# Porphyrins map calculation
por = reco[:, :, 21] * (51.8 / 30.5) - reco[:, :, 12]

# Displaying porphyrins map
plt.figure()
plt.imshow(por, cmap='gray', vmin=0, vmax=100)
plt.colorbar()
plt.axis('off')
plt.tight_layout()
picname = 'porp/porphyrin.jpg'
plt.savefig(picname, bbox_inches='tight')