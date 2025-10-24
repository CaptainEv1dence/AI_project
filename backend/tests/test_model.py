"""
Model functionality tests
"""
import pytest
from transformers import AutoModelForCausalLM, AutoTokenizer
from backend.main import MODEL_NAME, tokenizer, model


def test_model_loaded():
    """Test that model is loaded correctly"""
    assert model is not None
    # PreTrainedModel-relatedness check
    from transformers import PreTrainedModel
    assert isinstance(model, PreTrainedModel)

def test_tokenizer_loaded():
    """Test that tokenizer is loaded correctly"""
    assert tokenizer is not None
    # PreTrainedTokenizerBase-relatedness check
    from transformers import PreTrainedTokenizerBase
    assert isinstance(tokenizer, PreTrainedTokenizerBase)


def test_model_name():
    """Test that correct model is being used"""
    assert MODEL_NAME == "HuggingFaceTB/SmolLM2-135M-Instruct"


def test_tokenizer_encode_decode():
    """Test basic tokenizer functionality"""
    text = "Hello, world!"
    
    tokens = tokenizer.encode(text)
    assert len(tokens) > 0
    
    decoded = tokenizer.decode(tokens)
    assert "Hello" in decoded
    assert "world" in decoded
