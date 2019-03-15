def write_abayesqr_config(sam_filename, reference_filename, output):
  config_string = ("""filename of reference sequence (FASTA) : %s
filname of the aligned reads (sam format) : %s
paired-end (1 = true, 0 = false) : 0
SNV_thres : 0.01
reconstruction_start : 1
reconstruction_stop: 1300
min_mapping_qual : 60
min_read_length : 150
max_insert_length : 250
characteristic zone name : test
seq_err (assumed sequencing error rate(%%)) : 0.1
MEC improvement threshold : 0.0395 """ % (reference_filename, sam_filename) )
  with open(output, 'w') as config_file:
    config_file.write(config_string)

if __name__ == '__main__':
    write_abayesqr_config("acme.sam", "acme.fasta", "acme_config")

