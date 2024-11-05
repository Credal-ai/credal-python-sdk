# This file was auto-generated by Fern from our API Definition.

import typing
from .initial_chunk import InitialChunk
from .data_chunk import DataChunk
from .final_chunk import FinalChunk
from .blocked_chunk import BlockedChunk

StreamingChunk = typing.Union[InitialChunk, DataChunk, FinalChunk, BlockedChunk]
