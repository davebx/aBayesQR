# aBayesQR
aBayesQR is a viral quasispecies reconstruction algorithm that employs a maximum-likelihood framework to infer individual sequences in a mixture from high-throughput sequencing data. The search for the most likely quasispecies is conducted on long contigs constructed from the set of short reads, which enables identification of closely related haplotypes in a population and provides computational tractability of the Bayesian method. aBayesQR is the first method which is capable of detecting and reliably reconstructing viral haplotypes having very small mutual genetic distances.


Installation:
-------------

 1. Create a aBayesQR directory and download the compressed aBayesQR_v1.zip
    from https://github.com/SoYeonA/aBayesQR
 2. Uncompress aBayesQR_v1.zip into the directory.
 3. Enter aBayesQR directory run make


Data Preparation:
-----------------
Check config file format (configure to your setting)

* config file included in the package is configured to sample set 
* the aligned reads file (SAM format) and corresponding reference file (FASTA format) are required for quasispecies reconstruction


Running aBayesQR:
-----------------
Command : aBayesQR <config file> 

Output : <zone name>_ViralSeq.txt (reconstructed viral quasispecies and their frequencies are reported in text format)
