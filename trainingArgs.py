args_dict = {
    "model_name_or_path": 'google/byt5-small',
    "max_len": 128,
    "output_dir": './byt5-base-dutch-ocr-correction',
    "overwrite_output_dir": True,
    "per_device_train_batch_size": 2,
    "per_device_eval_batch_size": 2,
    "gradient_accumulation_steps": 4,
    "learning_rate": 5e-4,
    "warmup_steps": 250,
    "logging_steps": 100,
    "evaluation_strategy": "steps",
    "eval_steps": 250,
    "num_train_epochs": 4,
    "do_train": True,
    "do_eval": True,
    "fp16": False,
    "use_cache": False,
    "max_steps": 5000
}
parser = HfArgumentParser(
        (ModelArguments, DataTrainingArguments, TrainingArguments))
model_args, data_args, training_args = parser.parse_dict(args_dict)
set_seed(training_args.seed)