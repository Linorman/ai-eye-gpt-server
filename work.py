import mindspore
import mindspore.nn as nn
from mindnlp.models import GPT2PreTrainedModel, GPT2Config


class Work:
    def __init__(self):
        # self.network = GPT2PreTrainedModel(GPT2Config())
        # 导入模型参数
        mindspore.set_context(mode=mindspore.GRAPH_MODE)
        self.graph = mindspore.load("./static/model.mindir")
        self.model = nn.GraphCell(self.graph)

    def predict(self, inputs):
        # output = self.network(input_ids, input_mask, token_type_id)
        outputs = self.model(inputs)
        return outputs

