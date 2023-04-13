from recbole.quick_start import run_recbole

parameter_dict = {
   'train_neg_sample_args': None,
}
run_recbole(model='SASRec', dataset='ml-100k', config_dict=parameter_dict)
