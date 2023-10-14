# Liquidation Listener Protocol

## Description

This is a protocol for receiving information about liquidation events from a websocket stream.
It is based on the liquidation model [as defined here](https://github.com/marlinprotocol/mev-inspect-py/blob/main/mev_inspect/models/liquidations.py).

## Specification
---
name: liquidation_listener
author: zarathustra
version: 0.1.0
protocol_specification_id: zarathustra/liquidation_listener:0.1.0
description: A protocol for obtaining information on liquidation events.
license: Apache-2.0
aea_version: '>=1.0.0, <2.0.0'
speech_acts:
  subscribe_to_liquidation_events: {}
  unsubscribe_from_liquidation_events: {}
  liquidation_event:
    liquidated_user: pt:str
    liquidator_user: pt:str
    collateral_token_address: pt:str
    debt_token_address: pt:str
    debt_purchase_amount: pt:int
    received_amount: pt:int
    received_token_address: pt:optional[pt:str]
    protocol: ct:Protocol
    transaction_hash: pt:str
    trace_address: pt:list[pt:int]
    block_number: pt:str
  unsubscribed: {}
  error:
    error_code: ct:ErrorCode
    error_msg: pt:str
    error_data: pt:dict[pt:str, pt:str]
...
---
ct:Protocol: |
  enum ProtocolEnum {
    UNISWAP_V2 = 0;
    UNISWAP_V3 = 1;
    SUSHISWAP = 2;
    AAVE = 3;
    WETH = 4;
    CURVE = 5;
    ZERO_EX = 6;
    BALANCER_V1 = 7;
    COMPOUND_V2 = 8;
    CREAM = 9;
  }
  ProtocolEnum protocol = 1;
ct:ErrorCode: |
  enum ErrorCodeEnum {
      FAILED_TO_SUBSCRIBE = 0;
      FAILED_TO_UNSUBSCRIBE = 1;
    }
  ErrorCodeEnum error_code = 1;
...
---
initiation:
- subscribe_to_liquidation_events
- unsubscribe_from_liquidation_events
reply:
  subscribe_to_liquidation_events: [liquidation_event, error]
  unsubscribe_from_liquidation_events: [unsubscribed, error]
  liquidation_event: []
  unsubscribed: []
  error: []
roles: {client, server}
termination:
- liquidation_event
- unsubscribed
- error
end_states: [successful]
keep_terminal_state_dialogues: false
...
