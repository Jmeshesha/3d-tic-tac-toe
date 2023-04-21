using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class BoardGameObj : MonoBehaviour
{
    private char[] pieces = new char[] { 'r', 'g' };
    private int currPiece;
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
    // Start is called before the first frame update
    void Start()
    {
        gameboard = new Board(planes, rows, cols, inARow, pieces[0], pieces[1], ' ');
        currPiece = startingPiece;
        MakePlanes();


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
        }
    }
    


    private int OnPlacePiece(int plane, int row, int col)
    {
        int piecePlaced = -1;
        if(gameboard.PlacePiece(plane, row, col, pieces[currPiece])){
            piecePlaced = currPiece;
            currPiece = (currPiece + 1) % pieces.Length;
        }
        return piecePlaced;
    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
