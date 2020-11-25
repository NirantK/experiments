# experiments
Repository for Throwaway Code

Snippet to find lexically unique statements in a list of statements
```python
from fuzzywuzzy import fuzz
from typing import List

def get_uniques(sentence_list:List[str], threshold:int=51):
    uniques = [""]
    for sentence in sentence_list:
        scores = []
        for j in uniques:
            scores.append(fuzz.ratio(sentence, j))
        if max(scores) < threshold:
#             print(f"Found {len(uniques)} uniques so far")
            uniques.append(i)
```

Behaviour Note: Every statement that this finds is unique, but this does NOT find ALL unique statements. 

## Results for ShiftedReLU with Batchnorm removed experiments:

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

Links
---
- Code from trying out [gRPC in Python](https://www.semantics3.com/blog/a-simplified-guide-to-grpc-in-python-6c4e25f0c506/) in [weblearn](./weblearn)
- Adapted `try_fast_relu.ipynb` to try ELU instead of ReLU as suggested in [this paper](arxiv.org/pdf/1511.07289.pdf).
- [Supplemental Information on the Fast.ai forums](forums.fast.ai/t/shifted-relu-0-5/41467)
