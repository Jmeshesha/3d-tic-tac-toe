using System;
namespace Models
{
    [Serializable]
    class SerializableBoard
    {
        public int planes;
        public int rows;
        public int cols;
        public char currPlayer;
        public char opponent;
        public char emptyPiece;
        public float thinkTime;
        public int inARow;
        public string heuristic;
        public char[] board;

        public void SetupBoard(char[,,] oldboard)
        {
            planes = oldboard.GetLength(0);
            rows = oldboard.GetLength(1);
            cols = oldboard.GetLength(2);
            board = new char[planes * rows * cols];
            int boardIdx = 0;
            for(int i = 0; i < planes; i++) {
                for (int j = 0; j < rows; j++) {
                    for (int k = 0; k < cols; k++) {
                        board[boardIdx] = oldboard[i, j, k];
                        boardIdx++;
                    }
                }
            }
        }
        public char[,,] Get3dBoard()
        {
            char[,,] newboard = new char[planes, rows, cols];
            int boardIdx = 0;
            for (int i = 0; i < planes; i++)
            {
                for (int j = 0; j < rows; j++)
                {
                    for (int k = 0; k < cols; k++)
                    {
                        newboard[i, j, k] = board[boardIdx];
                        boardIdx++;
                    }
                }
            }
            return newboard;
        }


    }
}
