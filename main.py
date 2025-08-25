import openvino as ov
import utils
import numpy as np
from scipy.io.wavfile import write
from fastapi import FastAPI
from fastapi.responses import FileResponse
from urllib import parse
import time as t
from text import text_to_sequence
from hashlib import sha256
import os

app = FastAPI()
core = ov.Core()

config = {"PERFORMANCE_HINT": "LATENCY"}
pipe_tts = core.compile_model(core.read_model(model='models/all_base_ov.xml'), device_name="CPU", config=config)
conf_tts = utils.get_hparams_from_file('models/all_base.json')

@app.get("/tts", response_class=FileResponse, summary="Generate voice from text")
def tts(text = "", voice=31, lang='ko', static=0, isPlay=0):
    start = t.time()
    print(text, static)
    filename = f"output/{text}.wav"

    phoneme_ids = text_to_sequence(text, [f'canvers_{lang}_cleaners'])
    text = np.expand_dims(np.array(phoneme_ids, dtype=np.int64), 0)

    inputs = {
        "input": text,
        "input_lengths":  np.array([text.shape[1]], dtype=np.int64),
        "scales": np.array([0.667, 1.0, 0.8], dtype=np.float16),
        "sid" : np.array([int(voice)], dtype=np.int64) if voice is not None else None
    }

    start_time = t.time()
    result = pipe_tts(inputs)

    print(f"Inference time: {t.time() - start_time:.4f} seconds")

    audio = list(result.values())[0].squeeze((0, 1))  

    print(t.time() - start)
    
    write(data=audio, rate=conf_tts.data.sampling_rate, filename=filename)

    return filename