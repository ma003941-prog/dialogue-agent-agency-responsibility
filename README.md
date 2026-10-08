## Repository Contents

This repository is a continuation of 【https://github.com/w2430145/dialogue-agent-agency-responsibility 】which can no longer be maintained because access to the original account was lost.
This repository is structured into the following directories and files:

### `R_scripts/` (R Scripts)

This directory contains R scripts used for calculating Bayes Factors. These scripts were employed for Bayesian statistical hypothesis testing, specifically for rank-based tests such as the Wilcoxon Signed-Rank Test and Spearman's ρ correlation.

**Important Note:**

Some of the functions used within these R scripts, particularly the main samplers and helper functions for Bayes Factor calculation, are based on the methodology described in the following publication:

van Doorn, J., Ly, A., Marsman, M., & Wagenmakers, E.-J. (2020).
Bayesian rank-based hypothesis testing for the rank sum test,
the signed rank test, and Spearman's ρ.
*Journal of Applied Statistics, 47*(16), 2984-3006.
[https://doi.org/10.1080/02664763.2019.1709053]
To successfully run the code in this repository, you will need to separately obtain the R scripts provided with the original paper (e.g., `rankBasedCommonFunctions.R`, `signRankSampler.R`, `spearmanSampler.R`, `rankSumSampler.R`) and place them in the same directory as the R scripts in this repository. 

Included R scripts:
- `sota_likability.r`: Bayesian Wilcoxon Signed-Rank Test for pre-post difference in likability towards Sota.
- `spearman_agency_sota_responsibility.r`: Bayesian test of Spearman's correlation coefficient between agency attribution to Sota and responsibility attribution.
- `spearman_experience_aa_responsibility.r`: Bayesian test of Spearman's correlation coefficient between experience attribution to Sota and responsibility attribution to the agent adopter.
- `spearman_experience_sota_responsibility.r`: Bayesian test of Spearman's correlation coefficient between experience attribution to Sota and responsibility attribution to Sota.

### `Python_scripts/` (Python Scripts)

This directory contains Python scripts used for other data analyses.
- `the_effect_of_users__attribution_of_agency_toward_dialogue_agents_on_responsibility_attribution_to_agent_adopters_analysis.py`: Includes frequentist statistical tests such as the non-correlation test for Spearman's correlation coefficient and Wilcoxon Signed-Rank Test.

### `Experimental_Materials/` (Experimental Materials)

This directory contains materials used in the experiment.
- `Experimental Materials.docx`: instructions provided to participants, and questionnaire items in Japanese.

### `Raw_Data/` (Raw Data)

This directory contains the raw experimental results in CSV format.
All CSV files are encoded in UTF-8 with BOM.
The scales used in this raw data are based on the questionnaire items presented in the main paper for this repository: "The Effect of Users’ Attribution of Agency Toward Dialogue Agents on Responsibility Attribution to Agent Adopters."

Specifically, for items related to "Sota's capabilities" (Sotaは以下の項目をどの程度できると思いますか), the 7-point scale corresponds as follows:
- 日本語: 「1.非常にできない, 2.できない, 3.どちらかといえばできない, 4.どちらともいえない, 5.どちらかといえばよくできる, 6.よくできる, 7.非常によくできる」
- English: (1. Completely incapable, 2. Incapable, 3. Somewhat incapable, 4. Neutral, 5. Somewhat capable, 6. Capable, 7. Extremely capable)

For items related to "Attribution of Responsibility" (例: あなたが任務に失敗したのはSotaの責任だと思いますか？) and "Likability towards Agent Adopter (AA)" (AAに対する好感度), the 7-point scale corresponds as follows:
- 日本語: 「1.全くそう思わない, 2.そう思わない, 3.どちらかといえばそう思わない, 4.どちらでもない, 5.どちらかといえばそう思う, 6.そう思う, 7.非常にそう思う」
- English: (1 = Strongly disagree, 2 = Disagree, 3 = Slightly disagree, 4 = Neutral, 5 = Slightly agree, 6 = Agree, 7 = Strongly agree)

Additionally, the CSV files contain numerical data from the **Godspeed Scale III: Likability** questionnaire, used to assess impressions of Sota. The items were presented in the following order:

- 日本語:
    - 嫌い - 好き
    - 親しみにくい - 親しみやすい
    - 不親切な - 親切な
    - 不愉快な - 愉快な
    - 酷い - 良い
- English:
    - Dislike - Like
    - Unfriendly - Friendly
    - Unkind - Kind
    - Unpleasant - Pleasant
    - Awful - Nice
    
- `TypeA_Pre.csv`: Responses collected before the task for utterance Type A.
- `TypeA_Post.csv`: Responses collected after the task for utterance Type A.
- `TypeB_Pre.csv`: Responses collected before the task for utterance Type B.
- `TypeB_Post.csv`: Responses collected after the task for utterance Type B.


## Contact

If you have any questions or require further clarification, please feel free to contact Eiichiro Watanabe at [w2430145@gl.cc.uec.ac.jp].

