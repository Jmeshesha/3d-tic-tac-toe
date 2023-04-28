using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DynamicBackground : MonoBehaviour
{

    [SerializeField] private BoardGameObj boardManager;
    [SerializeField] private Material backgroundMat;

    [SerializeField] private float updateSpeed;

    [SerializeField] private float player1WinLerp;

    [SerializeField] private float player2WinLerp;
    private float targetLerpVal;
    private float[] playerWinLerp;

    // Start is called before the first frame update
    void Start()
    {
        backgroundMat.SetFloat("_LerpVal", boardManager.GetCurrPlayer());
        playerWinLerp = new float[]{ player1WinLerp, player2WinLerp};
        boardManager.PlayerWin += PlayerWin;
        boardManager.PlacePlayer += PlacePiece;
        boardManager.PlayerTie += PlayerTie;
    }

    // Update is called once per frame
    void Update()
    {
        UpdateShaderVal("_LerpVal", targetLerpVal, updateSpeed);
    }


    private void UpdateShaderVal(string fieldName, float target, float speed)
    {
        float currVal = backgroundMat.GetFloat(fieldName);

        float newVal = Mathf.Lerp(currVal, target, Time.deltaTime * speed);



        backgroundMat.SetFloat(fieldName, newVal);

    }

    private void PlacePiece(int nextplayer)
    {
        targetLerpVal = nextplayer;
    }

    private void PlayerWin(int player)
    {
        targetLerpVal = playerWinLerp[player];
    }

    private void PlayerTie()
    {
        targetLerpVal = 0.5f;
    }
}

