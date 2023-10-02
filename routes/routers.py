from fastapi import APIRouter
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

router = APIRouter(prefix="/router")


@router.get("/get_output_notebook")
async def get_output_notebook():
    # Carregar o notebook
    with open("notebook/") as f:
        nb = nbformat.read(f, as_version=4)

    # Executar o notebook
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': '/notebook/'}})

    # Obter a saída
    # Supondo que a saída é a última célula do notebook
    output = nb.cells[-1].outputs[0].data['text/plain']

    return {"output": output}
