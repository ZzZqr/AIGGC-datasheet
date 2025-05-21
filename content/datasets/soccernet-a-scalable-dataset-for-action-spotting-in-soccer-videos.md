---
title: "SoccerNet: A Scalable Dataset for Action Spotting in Soccer Videos"
subtitle: "CVPRW 2018"
tags: ["Sports", "Soccer"]
---

In this paper, we introduce SoccerNet, a benchmark for action spotting in soccer videos. The dataset is composed of 500 complete soccer games from six main European leagues, covering three seasons from 2014 to 2017 and a total duration of 764 hours. A total of 6,637 temporal annotations are automatically parsed from online match reports at a one minute resolution for three main classes of events (Goal, Yellow/Red Card, and Substitution). As such, the dataset is easily scalable. These annotations are manually refined to a one second resolution by anchoring them at a single timestamp following well-defined soccer rules. With an average of one event every 6.9 minutes, this dataset focuses on the problem of localizing very sparse events within long videos. We define the task of spotting as finding the anchors of soccer events in a video. Making use of recent developments in the realm of generic action recognition and detection in video, we provide strong baselines for detecting soccer events. We show that our best model for classifying temporal segments of length one minute reaches a mean Average Precision (mAP) of 67.8%. For the spotting task, our baseline reaches an Average-mAP of 49.7% for tolerances d ranging from 5 to 60 seconds. Our dataset and models are available at https://silviogiancola.github.io/SoccerNet.


<div style="margin-top: 1rem; padding: 1rem; display: inline-block;">

  <a href="https://doi.org/10.1109/cvprw.2018.00223" target="_blank" style="background-color: #0d9bdc; color: white; padding: 10px 16px; margin-right: 8px; text-decoration: none; border-radius: 4px; font-weight: bold;">
    Download Paper
  </a>

  <a href="../bib/soccernet-a-scalable-dataset-for-action-spotting-in-soccer-videos.bib" download style="background-color: #f0a500; color: white; padding: 10px 16px; text-decoration: none; border-radius: 4px; font-weight: bold;">
    Download BibTeX
  </a>

</div>
