# Replication package of Tracing the Lifecycle of Architecture Technical Debt in Software Systems: A Dependency Approach

## Description of this study:
Architectural technical debt (ATD) represents trade-offs in software architecture that accelerate initial development but create long-term maintenance challenges. ATD, in particular when self-admitted (SATD), impacts the foundational structure of software, making it difficult to detect and resolve.

This study investigates the lifecyle of ATD, focusing on how it affects i) the connectivity between classes, and ii) the frequency of file modifications. We aim to understand how ATD evolves from introduction to repayment, and its implications on software architectures.

Our empirical approach was applied to a dataset of SATD from various software artifacts, such as commit messages and issue tracking systems. We isolated ATD instances, filtered for architectural indicators, and calculated dependencies at different lifecycle stages using FAN-IN and FAN-OUT metrics. Statistical analyses, including the Mann-Whitney U test and Cohen’s d, were used to assess the significance and effect size of connectivity and dependency changes over time.

We observed that ATD repayment increased class connectivity, with FAN-IN increasing by 57\% on average and FAN-IN by 26.7%, suggesting a shift toward centralization and increased architectural complexity post-repayment. Moreover, ATD files were modified less frequently than Non-ATD files, with changes accumulated in high-dependency portions of the code.

Our study shows that resolving ATD improves software quality in the short-term, but can make the architecture more complex by centralizing dependencies. Also, even if dependency metrics (like FAN-IN and FAN-OUT) can be helpful for understanding the impact of ATD, they should be combined with other measures to capture other effects of ATD on software maintainability.

## Contents

### Dataset
- `atd_final.csv`\
    A CSV containing a list of the 18 ATD items from the trackers of five Apache open-source projects. From the 18 identified ATD items, we identified 5,135 files affected in the introduction phase and 3,553 files in the payment phase.
- `non_atd_final.csv`\
    A CSV containing a list of the 18 ATD items from the trackers of five Apache open-source projects. From the 18 identified Non-ATD items, we identified 753 files in the initial commit phase and 621 files in the recorded phase.

### Source code
1. **commit_hash_retrieval_with_date.py**: Script to extract commit hashes with a range of times from a Git repository.
2. **to_get_all_changes_updated.py**: Script for retrieving and listing all changes or updates in files between introduction and payment.
3. **und_count_file_dependencies.py**: Script for counting file dependencies using Understand by Scitools.
4. **golang-dependency.py**: Script to analyze and extract file dependencies in a Go (Golang) project.
5. **erlang-dependency.py**: Script to analyze and extract file dependencies in an Erlang project.
6. **file_path.csv**: CSV file containing file paths of ATD-affected files.
7. **calculate_sloc.py**: Script to calculate the Source Lines of Code (SLOC) for given ATD-affected files.
8. **lizard-cyclomatic-complexity.py**: Script for calculating cyclomatic complexity of source code using the Lizard library.
9. **data_distribution_log1p.py**: Script for analyzing and visualizing data distributions using a log(1+x) transformation.
10. **calculate_mean_median_min_max.py**: Script to calculate statistical values like mean, median, minimum, and maximum from a dataset.
11. **mann-whitney-u-test.py**: Script to perform the Mann-Whitney U test, a non-parametric test for comparing two independent samples.
12. **cohens_d.py**: Script for computing Cohen's d, a measure of effect size between two groups.
13. **boxplot_number_of_changes.py**: Script for generating a boxplot to visualize the number of changes in files.
14. **partial-spearmans-correlation.py**: Script for calculating partial Spearman’s correlation coefficients between introduction and payment. 
