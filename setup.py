from setuptools import find_packages,setup
from typing import List
HYPHEN_DOT='-e.'
def get_req(file_path:str)->List[str]:
    req=[]
    with open(file_path) as file_obj:
        req=file_obj.readlines()
        req=[i.replace("\n"," ") for i in req]
        
        if HYPHEN_DOT in req:
            req.remove(HYPHEN_DOT)
    return req
    
setup(
    name='mlproject',
    version='0.0.1',
    author='KA',
    packages=find_packages(),
    install_requires=get_req('req.txt')
)