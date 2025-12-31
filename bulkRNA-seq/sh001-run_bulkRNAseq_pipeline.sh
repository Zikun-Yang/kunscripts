#!/bin/bash

path="/mnt/disk1/primates_public_dataset/genomes/001-self_polished/human_T2T-CHM13v2.0"

nextflow run ~/pipeline/nextflow/rnaseq \
    --input samplesheet.csv \
    --outdir 002-bulkRNA_results \
    --gtf ${path}/T2T-CHM13v2.0.gtf \
    --fasta ${path}/T2T-CHM13v2.0.fa \
    -profile singularity \
    --skipBiotypeQC true \
    -c /home/zkyang/github_repo/nextflow_setting/high_resource_local.config \
    -resume
