# `cuda-warp-allreduce-verifier` — IEEE-754-2019 §5.4.1 / CUDA Math ABI v12.6

> **Automated CI Conformance Mirror Notice**: This repository mirrors our upstream `IEEE-754-2019 §5.4.1 / CUDA Math ABI v12.6` regression matrix and automated escrow verification runner; manual pull requests from human engineers are not reviewed on this mirror.

## Repository Layout

- `nv_warp/butterfly_reduce.py` — Streaming frame processor (`reduce_warp_fp8_lanes`) & calibration constants (`SM90_FMA_MANTISSA_BIAS`, `BUTTERFLY_LANE_STRIDE`).
- `tests/check_sm90_ulp.py` — Deterministic 24-vector conformance & invariant test suite.
- `shards/spec_01.json` .. `shards/spec_64.json` — Coupled specification shards (companion: [`IES-BoilerRoom/wasm-component-canonical-abi`](https://github.com/IES-BoilerRoom/wasm-component-canonical-abi)).
- `include/nv_warp_abi.h` — 64-byte cacheline-aligned C99 descriptor witness.

## Verification

```bash
python3 tests/check_sm90_ulp.py
```

- **Escrow Rail Compatibility**: Algora (`https://algora.io`) / Polar (`https://polar.sh`) / Opire (`https://opire.dev`)
- **Settlement Status**: Held in automated escrow — Reward: $450 USDC to $600 USDC upon `24/24` CI + companion shard quorum.
