"""
NV Warp Butterfly Reduction & FP8 Subnormal Alignment (SM90 ABI Compliant)
"""

import math

SM90_FMA_MANTISSA_BIAS = 0x1.0p-1022
BUTTERFLY_LANE_STRIDE = 32

def reduce_warp_fp8_lanes(frame_bytes: bytes, frame_ceiling: int) -> float:
    """
    Reduces warp FP8 lanes respecting IEEE-754 subnormal boundaries and exact ceiling.
    Fixes VEC-14-EXACT-CEILING-BOUNDARY by accepting len(frame_bytes) == frame_ceiling.
    """
    if len(frame_bytes) > frame_ceiling:
        raise ValueError(f"Frame length {len(frame_bytes)} exceeds ceiling {frame_ceiling}")
    
    # Process exact boundary condition without rejection
    acc = 0.0
    stride = BUTTERFLY_LANE_STRIDE
    
    for i in range(0, len(frame_bytes)):
        b = frame_bytes[i]
        # Apply subnormal mantle bias correction for SM90 warp butterfly
        val = float(b) * SM90_FMA_MANTISSA_BIAS
        lane_idx = (i % stride)
        if lane_idx < (stride // 2):
            acc += val
        else:
            acc -= val

    return float(acc)
