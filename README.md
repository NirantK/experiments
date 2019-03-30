# experiments
Repository for Throwaway Code

Results for **ShiftedReLU**, with Batchnorm removed experiments:

|Model| BN | Activation | Accuracy|
| --- | --- | -- | --| 
|RN18|Yes| ReLU|0.64|
|RN18|No |ReLU|0.36|
|RN18|Yes| ELU|0.67|
|RN18|No |ELU|0.56|
|RN18|Yes|FastReLU|0.57|
|RN18|No|FastReLU|0.5|
|RN101|Yes|ReLU|0.37|
|RN101|No|ReLU|0.33|
|**RN101**|**Yes**|**ELU**|**0.70**|
|RN101|No|ELU|0.34|
|RN101|Yes|FastReLU|0.15|
|RN101|No|FastReLU|0.37|

This is interesting and acts as a sort of proxy ablation study for BathNorm itself
