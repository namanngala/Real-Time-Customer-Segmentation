from setuptools import find_packages,setup
from typing import List

HyphenE = "-e ."
def get_requirements(find_path:str)->List[str]:
    requirements = []
    with open(find_path) as f:
        requirements= f.readlines()
        requirements = [r.replace("\n", "") for r in requirements]
        
        if HyphenE in requirements:
            requirements = requirements.remove(HyphenE)
    return requirements
        

setup(
name='Real-Time-Customer-Segmentation-with-Scalable-Kubernetes-Deployment-and-CI-CD-Integration',
version='0.0.1',
author='Naman Gala',
author_email='namangala2000@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)