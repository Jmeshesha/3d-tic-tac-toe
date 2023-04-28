using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using Models;


public class BoardGameObj : MonoBehaviour
{
    public delegate void OnPlayerAction(int player);

    public OnPlayerAction PlayerWin;
    public OnPlayerAction PlacePlayer;

    public Action PlayerTie;

    private char[] pieces = new char[] { 'r', 'g' };
    private char emptyPiece = ' ';
    public int currPiece;
    private Board gameboard;
    [SerializeField] private int planes;

    [SerializeField] private int rows;

    [SerializeField] private int cols;
    [SerializeField] [Range(0, 1)] private int startingPiece = 0; 
    [SerializeField] private int inARow;

    [SerializeField] private float planeSpacing;
    [SerializeField] private float pieceSize;
    [SerializeField] private float planeThickness;

    [SerializeField] private BoardPlane planePrefab;

    [SerializeField] private Piece piecePrefab;
    private List<Models.Move> moveHistory;

    private bool gameOver;

    private List<BoardPlane> planeList = new List<BoardPlane>();
    // Start is called before the first frame update
    void Start()
    {
        gameboard = new Board(planes, rows, cols, inARow, pieces[0], pieces[1], emptyPiece);
        currPiece = startingPiece;
        MakePlanes();
        gameOver = false;
        moveHistory = new List<Move>();
    }

    public char GetEmptyPiece()
    {
        return emptyPiece;
    }
    private void MakePlanes()
    {
        for (int i = 0; i < planes; i++)
        {
            Vector3 pos = Vector3.zero;
            Vector3 scale = Vector3.one;
            scale.x = rows * pieceSize;
            scale.y = planeThickness;
            scale.z = cols * pieceSize;

            pos.y = (i - (planes - 1) / 2) * planeSpacing;
            BoardPlane plane = Instantiate(planePrefab, transform);
            plane.gameObject.transform.localPosition = pos;
            plane.gameObject.transform.localScale = scale;
            plane.Setup(i, rows, cols, pieceSize, true, piecePrefab);
            planeList.Add(plane);
        }
    }



    public bool PlacePiece(Piece piece, int player)
    {
        if (gameOver || currPiece != player)
        {
            return false;
        }
        Vector3Int position = piece.GetCoords();
        if (!gameboard.PlacePiece(position.x, position.y, position.z, pieces[player]))
        {

            return false;
        }

        piece.ShowPiece(player);
        currPiece = (currPiece + 1) % pieces.Length;
        
        if (gameboard.IsWinAt(position.x, position.y, position.z, pieces[player]))
        {
            gameOver = true;
            PlayerWin?.Invoke(player);
        }
        else if (gameboard.IsTie())
        {
            gameOver = true;
            PlayerTie?.Invoke();
        } else
        {
            PlacePlayer?.Invoke(currPiece);
        }

        moveHistory.Add(new Move()
        {
            player = pieces[player],
            plane = position.x,
            row = position.y,
            col = position.z
        }); 
        return true;
    }

    public List<Move> GetMoveHistory()
    {
        return moveHistory;
    }

    public int GetPlayerIdx(char player)
    {
        if (player.Equals(pieces[0])){
            return 0;
        } else if(player.Equals(pieces[0]))
        {
            return 1;
        }
        return -1;
    }
    public char[,,] GetBoard()
    {
        return gameboard.GetBoard();
    }

    public char GetPlayerChar(int player)
    {
        if(player < 0 || player > 1)
        {
            return ' ';
        }
        return pieces[player];
    }

    public bool PlacePiece(int plane, int row, int col, int player)
    {
        Piece piece = planeList[plane].GetPiece(row, col);

        

        return PlacePiece(piece, player);
    }

    public int GetCurrPlayer()
    {
        return currPiece;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
