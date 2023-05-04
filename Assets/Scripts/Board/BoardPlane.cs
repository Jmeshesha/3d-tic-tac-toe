using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BoardPlane : MonoBehaviour
{
    public delegate int OnPiecePlaced(int plane, int row, int col);
    public event OnPiecePlaced onPlacePiece;

    private Piece[,] plane;

    


    private int planeIdx;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    private void MakePieces(int rows, int cols, Piece piecePrefab, float pieceSize)
    {
        plane = new Piece[rows, cols];
        for (int i = 0; i < rows; i++)
        {
            for(int j = 0; j < cols; j++)
            {
                Vector3 pos = Vector3.zero;
                Vector3 scale = Vector3.one * pieceSize;
                scale.x /= transform.localScale.x;
                scale.y /= transform.localScale.y;
                scale.z /= transform.localScale.z;
                pos.x = (i - (rows-1) / 2.0f) * pieceSize;
                pos.z = (j - (cols-1) / 2.0f) * pieceSize;
                plane[i, j] = Instantiate(piecePrefab, transform);
                plane[i, j].gameObject.transform.position = pos + transform.position;
                plane[i, j].gameObject.transform.localScale = scale;
                plane[i, j].Setup(planeIdx, i, j);

            }
        }
    }


    public void Setup(int planeIdx, int rows, int cols, float pieceSize, bool canHover, Piece piecePrefab)
    {
        GetComponent<Renderer>().material.SetFloat("_Rows", rows);
        GetComponent<Renderer>().material.SetFloat("_Columns", cols);
        this.planeIdx = planeIdx;

        MakePieces(rows, cols, piecePrefab, pieceSize);
        

    }
    public void Teardown(){
        for (int i = 0; i < plane.GetLength(0); i++)
        {
            for(int j = 0; j < plane.GetLength(1); j++)
            {
                Destroy(plane[i, j]);
            }
        }
        Destroy(this);
    }

    private void PlacePiece(int row, int col)
    {
        int piecePlaced = onPlacePiece.Invoke(planeIdx, row, col);
        if (piecePlaced == -1)
        {
            return;
        }


    }

    public Piece GetPiece(int row, int col)
    {
        return plane[row, col];
    }

    
}
