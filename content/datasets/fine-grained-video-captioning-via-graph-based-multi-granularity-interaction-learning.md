---
title: "Fine-Grained Video Captioning via Graph-based Multi-Granularity Interaction Learning"
subtitle: "T-PAMI 2022"
tags: ["Sports", "Basketball"]
---

Learning to generate continuous linguistic descriptions for multi-subject interactive videos in great details has particular applications in team sports auto-narrative. In contrast to traditional video caption, this task is more challenging as it requires simultaneous modeling of fine-grained individual actions, uncovering of spatio-temporal dependency structures of frequent group interactions, and then accurate mapping of these complex interaction details into long and detailed commentary. To explicitly address these challenges, we propose a novel framework <italic>Graph-based Learning for Multi-Granularity Interaction Representation (GLMGIR)</italic> for fine-grained team sports auto-narrative task. A multi-granular interaction modeling module is proposed to extract among-subjects&#x2019; interactive actions in a progressive way for encoding both intra- and inter-team interactions. Based on the above multi-granular representations, a multi-granular attention module is developed to consider action/event descriptions of multiple spatio-temporal resolutions. Both modules are integrated seamlessly and work in a collaborative way to generate the final narrative. In the meantime, to facilitate reproducible research, we collect a new video dataset from <italic>YouTube.com</italic> called Sports Video Narrative dataset (SVN). It is a novel direction as it contains <inline-formula><tex-math notation="LaTeX">$6K$</tex-math><alternatives><mml:math><mml:mrow><mml:mn>6</mml:mn><mml:mi>K</mml:mi></mml:mrow></mml:math><inline-graphic xlink:href="zhuang-ieq1-2946823.gif"/></alternatives></inline-formula> team sports videos (i.e., NBA basketball games) with <inline-formula><tex-math notation="LaTeX">$10K$</tex-math><alternatives><mml:math><mml:mrow><mml:mn>10</mml:mn><mml:mi>K</mml:mi></mml:mrow></mml:math><inline-graphic xlink:href="zhuang-ieq2-2946823.gif"/></alternatives></inline-formula> ground-truth narratives(e.g., sentences). Furthermore, as previous metrics such as METEOR (i.e., used in coarse-grained video caption task) DO NOT cope with fine-grained sports narrative task well, we hence develop a novel evaluation metric named Fine-grained Captioning Evaluation (FCE), which measures how accurate the generated linguistic description reflects fine-grained action details as well as the overall spatio-temporal interactional structure. Extensive experiments on our SVN dataset have demonstrated the effectiveness of the proposed framework for fine-grained team sports video auto-narrative.


<div style="margin-top: 1rem; padding: 1rem; display: inline-block;">

  <a href="https://doi.org/10.1109/TPAMI.2019.2946823" target="_blank" style="background-color: #0d9bdc; color: white; padding: 10px 16px; margin-right: 8px; text-decoration: none; border-radius: 4px; font-weight: bold;">
    Download Paper
  </a>

  <a href="bib/fine-grained-video-captioning-via-graph-based-multi-granularity-interaction-learning.bib" download style="background-color: #f0a500; color: white; padding: 10px 16px; text-decoration: none; border-radius: 4px; font-weight: bold;">
    Download BibTeX
  </a>

</div>
