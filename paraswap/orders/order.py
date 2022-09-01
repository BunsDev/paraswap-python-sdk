from web3 import Web3

from paraswap.config import AUGUSTUS
from paraswap.types import Network

from ..constants import MAX_UINT256_VALUE
from .types import Order, OrderNFT
from .utils import (
    AssetType,
    encode_asset_address_with_asset_type,
    generate_nonce_and_add_taker,
    random_uint,
)


def create_order(
    expiry: int,
    maker: str,
    taker: str,
    maker_asset: str,
    taker_asset: str,
    maker_amount: int,
    taker_amount: int,
    nonce_and_meta: int = -1,
) -> Order:
    if nonce_and_meta == -1:
        nonce_and_meta = random_uint(MAX_UINT256_VALUE)

    return Order(
        nonceAndMeta=nonce_and_meta,
        expiry=expiry,
        maker=Web3.toChecksumAddress(maker),
        taker=Web3.toChecksumAddress(taker),
        makerAsset=Web3.toChecksumAddress(maker_asset),
        takerAsset=Web3.toChecksumAddress(taker_asset),
        makerAmount=maker_amount,
        takerAmount=taker_amount,
    )


def create_managed_order(
    network: Network,
    expiry: int,
    maker: str,
    maker_asset: str,
    taker_asset: str,
    maker_amount: int,
    taker_amount: int,
    actual_taker: str,
):
    # encode taker address inside the nonce and meta and generate a random nonce
    nonce_and_meta = generate_nonce_and_add_taker(actual_taker)
    return create_order(
        expiry=expiry,
        maker=maker,
        taker=AUGUSTUS[network],  # ParaSwap managed orders ALWAYS go through AUGUSTUS
        maker_asset=maker_asset,
        taker_asset=taker_asset,
        maker_amount=maker_amount,
        taker_amount=taker_amount,
        nonce_and_meta=nonce_and_meta,
    )


def create_managed_p2p_order(
    network: Network,
    expiry: int,
    maker: str,
    maker_asset: str,
    taker_asset: str,
    maker_amount: int,
    taker_amount: int,
    actual_taker: str,
):
    # encode taker address inside the nonce and meta and generate a random nonce
    nonce_and_meta = generate_nonce_and_add_taker(actual_taker)
    return create_order(
        expiry=expiry,
        maker=maker,
        taker=AUGUSTUS[network],  # ParaSwap managed orders ALWAYS go through AUGUSTUS
        maker_asset=maker_asset,
        taker_asset=taker_asset,
        maker_amount=maker_amount,
        taker_amount=taker_amount,
        nonce_and_meta=nonce_and_meta,
    )


def create_order_nft(
    maker: str,
    taker: str,
    maker_asset: str,
    maker_asset_type: AssetType,
    taker_asset: str,
    taker_asset_type: AssetType,
    maker_amount: int,
    taker_amount: int,
    maker_asset_id: int = 0,
    taker_asset_id: int = 0,
    nonce_and_meta: int = -1,
) -> OrderNFT:
    if nonce_and_meta == -1:
        nonce_and_meta = random_uint(MAX_UINT256_VALUE)

    return OrderNFT(
        nonceAndMeta=nonce_and_meta,
        maker=Web3.toChecksumAddress(maker),
        taker=Web3.toChecksumAddress(taker),
        makerAsset=encode_asset_address_with_asset_type(maker_asset, maker_asset_type),
        makerAssetId=maker_asset_id,
        takerAsset=encode_asset_address_with_asset_type(taker_asset, taker_asset_type),
        takerAssetId=taker_asset_id,
        makerAmount=maker_amount,
        takerAmount=taker_amount,
    )


def create_managed_order_nft(
    maker: str,
    taker: str,
    maker_asset: str,
    maker_asset_type: AssetType,
    taker_asset: str,
    taker_asset_type: AssetType,
    maker_amount: int,
    taker_amount: int,
    actual_taker: str,
    maker_asset_id: int = 0,
    taker_asset_id: int = 0,
) -> OrderNFT:
    # encode taker address inside the nonce and meta and generate a random nonce
    nonce_and_meta = generate_nonce_and_add_taker(actual_taker)
    return create_order_nft(
        maker=maker,
        taker=taker,
        maker_asset=maker_asset,
        maker_asset_type=maker_asset_type,
        taker_asset=taker_asset,
        taker_asset_type=taker_asset_type,
        maker_amount=maker_amount,
        taker_amount=taker_amount,
        maker_asset_id=maker_asset_id,
        taker_asset_id=taker_asset_id,
        nonce_and_meta=nonce_and_meta,
    )
