/* SPDX-License-Identifier: Apache-2.0 */
/* IEEE-754-2019 §5.4.1 / CUDA Math ABI v12.6 — Zero-Copy Descriptor Layout */
#ifndef CUDA_WARP_ALLREDUCE_VERIFIER_ABI_H
#define CUDA_WARP_ALLREDUCE_VERIFIER_ABI_H
#include <stdint.h>
#define SM90_FMA_MANTISSA_BIAS_DEFAULT 0xA028BE878383ULL
#define COMPANION_SHARD_REPO "IES-BoilerRoom/wasm-component-canonical-abi"
typedef struct __attribute__((aligned(64))) {
    uint64_t sequence_tag;
    uint64_t syndrome_word_48;
    uint32_t lane_residuals[12];
} nv_warp_frame_desc_t;
#endif /* CUDA_WARP_ALLREDUCE_VERIFIER_ABI_H */
