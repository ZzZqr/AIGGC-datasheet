---
title: "Understanding Game-Playing Agents with Natural Language Annotations"
subtitle: "ACL 2022"
tags: ["Board", "Go"]
---

We present a new dataset containing 10K human-annotated games of Go and show how these natural language annotations can be used as a tool for model interpretability. Given a board state and its associated comment, our approach uses linear probing to predict mentions of domain-specific terms (e.g., ko, atari) from the intermediate state representations of game-playing agents like AlphaGo Zero. We find these game concepts are nontrivially encoded in two distinct policy networks, one trained via imitation learning and another trained via reinforcement learning. Furthermore, mentions of domain-specific terms are most easily predicted from the later layers of both models, suggesting that these policy networks encode high-level abstractions similar to those used in the natural language annotations.


<div style="margin-top: 1rem; padding: 1rem; display: inline-block;">

  <a href="https://aclanthology.org/2022.acl-short.90/" target="_blank" style="background-color: #0d9bdc; color: white; padding: 10px 16px; margin-right: 8px; text-decoration: none; border-radius: 4px; font-weight: bold;">
    Download Paper
  </a>

  <a href="bib/understanding-game-playing-agents-with-natural-language-annotations.bib" download style="background-color: #f0a500; color: white; padding: 10px 16px; text-decoration: none; border-radius: 4px; font-weight: bold;">
    Download BibTeX
  </a>

</div>
