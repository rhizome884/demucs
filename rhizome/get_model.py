from demucs import pretrained
from demucs.apply import apply_model
bag = pretrained.get_model('htdemucs')    # for a bag of models or a named model
                                          # (which is just a bag with 1 model).
#model = pretrained.get_model('955717e8')  # using the signature for single models.
model = pretrained.get_model('5c90dfd2')

print(model)
#bag.models                       # list of individual models
#stems = apply_model(model, mix)  # apply the model to the given mix.
