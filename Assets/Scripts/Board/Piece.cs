using System.Collections;

using UnityEngine;


public class Piece : MonoBehaviour
{


    
    private Vector3Int coordinates;
    private int hoverAlphaTarget = 0;
    private int hoverStrengthTarget = 10;
    private float hoverAlphaThreshhold = 0.01f;
    public float hoverStrengthThreshhold = 0.01f;


    private int matAlphaTarget = 0;
    private float matAlphaThreshhold = 0.01f;
    [SerializeField] private int matAlphaSpeed;

    [SerializeField] private float hoverAlphaSpeed;
    [SerializeField] private float hoverStrengthSpeed;


    private int hoverState = 0;

    private Material pieceMat;

    private void Awake()
    {
        
    }
    // Start is called before the first frame update
    void Start()
    {
        pieceMat = gameObject.GetComponent<MeshRenderer>().material;
    }

    // Update is called once per frame
    void Update()
    {
        UpdateShaderVal("_OutlineAlpha", hoverAlphaTarget, hoverAlphaThreshhold, hoverAlphaSpeed);
        UpdateShaderVal("_OutlineStrength", hoverStrengthTarget, hoverStrengthThreshhold, hoverStrengthSpeed);
        UpdateShaderVal("_Alpha", matAlphaTarget, matAlphaThreshhold, matAlphaSpeed);
    }


    private void UpdateShaderVal(string fieldName, float target, float threshold, float speed)
    {
        float currVal = pieceMat.GetFloat(fieldName);

        float newVal = Mathf.Lerp(currVal, target, Time.deltaTime * speed);
        

        if (Mathf.Abs(newVal - target) < threshold) {
            pieceMat.SetFloat(fieldName, target);
        } else {
            pieceMat.SetFloat(fieldName, newVal);
        }

    }


    public void Hover()
    {
        hoverAlphaTarget = 1;
        hoverStrengthTarget = 1;
    }



    public void UnHover()
    {
        hoverAlphaTarget = 0;
        hoverStrengthTarget = 10;
    }


    public void Setup(int plane, int row, int col)
    {
        coordinates = new Vector3Int(plane, row, col);
    }

    public Vector3Int GetCoords()
    {
        return coordinates;
    }

    public void ShowPiece(int player)
    {
        pieceMat.SetFloat("_PlayerLerp", player);
        matAlphaTarget = 1;

    }
    
    public void HidePiece()
    {
        matAlphaTarget = 0;
    }
}
