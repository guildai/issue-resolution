import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(
    version_base=None,
    config_path='embeddings_and_difficulty/configs_hydra',
    config_name='config.yaml',
)
def main(args: DictConfig):
    print(OmegaConf.to_yaml(args))

if __name__ == "__main__":
    main()
