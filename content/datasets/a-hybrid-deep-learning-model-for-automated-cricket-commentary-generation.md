---
title: "A Hybrid Deep Learning Model for Automated Cricket Commentary Generation"
subtitle: "ICCCMLA 2024"
tags: ["Sports", "Cricket"]
---

The paper proposes an innovative method for generating cricket commentary. A hybrid model is proposed that combines three types of neural networks: Convolutional Neural Networks (CNN) for image processing, Long Short-Term Memory (LSTM) networks for sequential text generation, and Graph Convolutional Networks (GCN) for semantic understanding. By integrating these components, the model can generate ball-by-ball commentary that is coherent and contextaware. The model works by processing video frames from a cricket match using CNN. The resulting feature maps are used to retain essential visual information. Fully connected layers transform the features to a format suitable for input into the LSTM. The LSTM generates one word at a time, considering the temporal dependencies inherent in ball-by-ball events. To enhance the semantic understanding between the generated captions, the GCN is used. Evaluation metrics like BLEU, METEOR, and ROUGE are used to assess the proficiency of the model.



<div style="margin-top: 1rem; padding: 1rem; display: inline-block;">

  <a href="https://doi.org/10.1109/ICCCMLA63077.2024.10871604" target="_blank" style="background-color: #0d9bdc; color: white; padding: 10px 16px; margin-right: 8px; text-decoration: none; border-radius: 4px; font-weight: bold;">
    Download Paper
  </a>

  <a href="../bib/a-hybrid-deep-learning-model-for-automated-cricket-commentary-generation.bib" download style="background-color: #f0a500; color: white; padding: 10px 16px; text-decoration: none; border-radius: 4px; font-weight: bold;">
    Download BibTeX
  </a>

</div>
