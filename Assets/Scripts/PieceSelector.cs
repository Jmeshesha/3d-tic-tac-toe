using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PieceSelector : MonoBehaviour
{
    public float selectionDistance;
    Piece selectedPiece;
    public LayerMask pieceLayer;
    private Camera camera;

    [SerializeField] private BoardGameObj boardManager;
    
    // Start is called before the first frame update
    void Start()
    {
        selectedPiece = null;
        camera = GetComponent<Camera>();
    }

    // Update is called once per frame
    void Update()
    {
        CheckForHover();
        if (Input.GetMouseButton(0) && selectedPiece != null)
        {
            boardManager.PlacePiece(selectedPiece, 1);
        }
    }

    
    public void CheckForHover()
    {
        Ray ray = camera.ScreenPointToRay(Input.mousePosition);
        RaycastHit hit;
        if(Physics.Raycast(ray, out hit, Mathf.Infinity, pieceLayer)){
            Piece hitPiece;
            if(hit.transform.gameObject.TryGetComponent<Piece>(out hitPiece))
            {
                selectedPiece?.UnHover();
                hitPiece.Hover();
                selectedPiece = hitPiece;
            }
        }else if(selectedPiece != null) {
            selectedPiece.UnHover();
            selectedPiece = null;
        }
    }
}
