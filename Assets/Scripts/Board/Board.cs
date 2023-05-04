using UnityEngine;
using System;
using System.Collections.Generic;

class Board
{
    public delegate void OnPlaced(int plane, int row, int col);
    public event OnPlaced PeicePlaced;
    char redPlayer;
    char greenPlayer;
    char emptySpot;
    private int inARow;
    private char[,,] gameBoard;

    public Board(int planes, int rows, int columns, int inARow, char redPlayer, char greenPlayer, char emptySpot)
    {
        gameBoard = new char[planes, rows, columns];
        this.inARow = inARow;
        this.emptySpot = emptySpot;
        this.redPlayer = redPlayer;
        this.greenPlayer = greenPlayer;
        SetBoard(emptySpot);
    }

    public Board(char[,,] board, int inARow, char redPlayer, char greenPlayer, char emptySpot)
    {
        this.inARow = inARow;
        this.emptySpot = emptySpot;
        this.redPlayer = redPlayer;
        this.greenPlayer = greenPlayer;
        gameBoard = GetBoardCopy(board);
    }

    private void SetBoard(char spot)
    {
        for (int plane = 0; plane < gameBoard.GetLength(0); plane++)
        {
            for (int row = 0; row < gameBoard.GetLength(1); row++)
            {
                for (int col = 0; col < gameBoard.GetLength(2); col++)
                {
                    gameBoard[plane, row, col] = spot;
                }
            }
        }
    }

    public char GetPeice(int plane, int row, int col)
    {
        return gameBoard[plane, row, col];
    }

    private char[,,] GetBoardCopy(char[,,] oldboard)
    {
        int planes = oldboard.GetLength(0);
        int rows = oldboard.GetLength(1);
        int cols = oldboard.GetLength(2);
        char[,,] newBoard = new char[planes, rows, cols];
        for (int plane = 0; plane < planes; plane++)
        {
            for (int row = 0; row < rows; row++)
            {
                for (int col = 0; col < cols; col++)
                {
                    char oldPiece = oldboard[plane, row, col];
                    if(!(oldPiece.Equals(redPlayer) || oldPiece.Equals(greenPlayer) || oldPiece.Equals(emptySpot)))
                    {
                        string errorMsg = string.Format("Piece at ({0}, {1}, {2}) is an invalid character!", plane, row, col);
                        throw new InvalidOperationException(errorMsg);
                    }
                    newBoard[plane, row, col] = oldboard[plane,row,col];
                }
            }
        }
        return newBoard;
    }

    

    public bool InBounds(int plane, int row, int col)
    {
        bool planeInBounds = plane >= 0 && plane < gameBoard.GetLength(0);
        bool rowInBounds = row >= 0 && row < gameBoard.GetLength(1);
        bool colInBounds = col >= 0 && col < gameBoard.GetLength(2);


        return planeInBounds && rowInBounds && colInBounds;
    }

    public char[,,] GetBoard()
    {
        return GetBoardCopy(gameBoard);
    }
    

    private bool CheckWin(Vector3Int pos, Vector3Int delta, char player)
    {
        if (!InBounds(pos.x, pos.y, pos.z) || !gameBoard[pos.x, pos.y, pos.z].Equals(player))
        {
            return false;
        }
        int inARowCount = 1;
        Vector3Int currPos = pos + delta;
        // check positive delta direction
        while (InBounds(currPos.x, currPos.y, currPos.z) && gameBoard[currPos.x, currPos.y, currPos.z].Equals(player))
        {
            inARowCount += 1;
            currPos += delta;
        }

        delta *= -1;
        currPos = pos + delta;


        // check negative delta direction
        while (InBounds(currPos.x, currPos.y, currPos.z) && gameBoard[currPos.x, currPos.y, currPos.z].Equals(player))
        {
            inARowCount += 1;
            currPos += delta;
        }

        return inARowCount >= inARow;
    }

    public bool PlacePiece(int plane, int row, int col, char piece)
    {
        bool isValidPlayer = piece.Equals(redPlayer) || piece.Equals(greenPlayer);
        if (gameBoard[plane, row, col].Equals(emptySpot) && isValidPlayer)
        {
            gameBoard[plane, row, col] = piece;

            return true;
        }
        return false;
    }
    public bool RemovePiece(int plane, int row, int col)
    {
        if (!gameBoard[plane, row, col].Equals(emptySpot))
        {
            gameBoard[plane, row, col] = emptySpot;

            return true;
        }
        return false;
    }


    public bool IsTie()
    {
        for(int plane = 0; plane < gameBoard.GetLength(0); plane++)
        {
            for (int row = 0; row < gameBoard.GetLength(1); row++)
            {
                for (int col = 0; col < gameBoard.GetLength(2); col++)
                {
                    char piece = gameBoard[plane, row, col];
                    if(!piece.Equals(redPlayer) && !piece.Equals(greenPlayer))
                    {
                        return false;
                    }
                }
            }
        }
        return true;
    }


    public bool IsWinAt(int plane, int row, int col, char player)
    {
        if (!InBounds(plane, row, col))
        {
            return false;
        }

        Vector3Int pos = new Vector3Int(plane, row, col);

        for (int deltaPlane = -1; deltaPlane <= 1; deltaPlane++)
        {
            for (int deltaRow = -1; deltaRow <= 1; deltaRow++)
            {
                for (int deltaCol = -1; deltaCol <= 1; deltaCol++)
                {
                    Vector3Int delta = new Vector3Int(deltaPlane, deltaRow, deltaCol);
                    if (delta.magnitude >= 1 && CheckWin(pos, delta, player))
                    {
                        return true;
                    }
                }
            }
        }


        return false;

    }
}

