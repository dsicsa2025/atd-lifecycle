# Replication package of Tracing the Lifecycle of Architecture Technical Debt in Software Systems: A Dependency Approach

## Description of this study:
Architectural technical debt (ATD) represents trade-offs in software architecture that accelerate initial development but create long-term maintenance challenges. ATD, in particular when self-admitted (SATD), impacts the foundational structure of software, making it difficult to detect and resolve.

This study investigates the lifecyle of ATD, focusing on how it affects i) the connectivity between classes, and ii) the frequency of  file modifications. We aim to understand how ATD evolves from introduction to repayment, and its implications on software architectures.

Our empirical approach was applied to a dataset of SATD from various software artifacts, such as commit messages and issue tracking systems. We isolated ATD instances, filtered for architectural indicators, and calculated dependencies at different lifecycle stages using FAN-IN and FAN-OUT metrics. Statistical analyses, including the Mann-Whitney U test and Cohen’s \textit{d}, were used to assess the significance and effect size of connectivity and dependency changes over time.

We observed that ATD repayment increased class connectivity, with FAN-IN increasing by 57\% on average and FAN-IN by 26.7\%, suggesting a shift toward centralization and increased architectural complexity post-repayment. Moreover, ATD files were modified more frequently than Non-ATD files, with changes accumulated in high-dependency portions of the code.

Resolving ATD improves software quality in the short-term but can make the architecture more complex by centralizing dependencies. Even if dependency metrics (like FAN-IN and FAN-OUT) can be helpful for understanding the impact of ATD, they should be combined with other measures to capture other effects of ATD on software maintainability.
