using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Models;
using System;
using Proyecto26;

public class AIPlayer : MonoBehaviour
{
    [SerializeField] private BoardGameObj gameboardManager;

    [SerializeField] private string basePath;
    [SerializeField] private float thinkTime;
    [SerializeField] private int port;
    [SerializeField] [Range(0, 1)] private int playerIdx;
    private bool isTurn = false;
    // Start is called before the first frame update
    void Start()
    {
        gameboardManager.PlacePlayer += OnPlacePiece;
        isTurn = false;
    }

    // Update is called once per frame
    void Update()
    {
        if (isTurn) {
            //PlaceMoveFromAi();
            isTurn = false;
        }
    }

    public void OnPlacePiece(int piece)
    {
        
        if(piece != playerIdx)
        {
            return;
        }
        isTurn = true;
    }

    private void PlaceMoveFromAi()
    {
        SerializableBoard board = new SerializableBoard();
        board.SetupBoard(gameboardManager.GetBoard());
        board.currPlayer = gameboardManager.GetPlayerChar(playerIdx);
        board.emptyPiece = gameboardManager.GetEmptyPiece();
        board.thinkTime = thinkTime;
        RequestHelper request = new RequestHelper
        {
            Uri = basePath + "/GetAiMove",
            Body = board,
            EnableDebug = true
        };
        RestClient.Post<Move>(request).Then(res =>
        {
            if(!gameboardManager.PlacePiece(res.plane, res.row, res.col, playerIdx))
            {
                string errorMsg = string.Format("Could not place piece at ({0}, {1}, {2})", res.plane, res.row, res.col);
                throw new InvalidOperationException(errorMsg);
            }
        });
    }
}
