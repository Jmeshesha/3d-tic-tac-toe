using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using Cinemachine.Utility;

public class Movement : MonoBehaviour
{
    [SerializeField]
    private float mouseRotateSpeed;
    
    [SerializeField]
    private float initMousePush;

   


    [SerializeField]
    private float rotateMaxSpeed;
    private Vector2 prevMousePos;



    private bool holding = false;

    private Vector3 anchor;
    private Vector3 heldEuler;
    // Start is called before the first frame update
    void Start()
    {
        //UpdateAnchor();
    }

    // Update is called once per frame
    void Update()
    {
        if(IsHolding())
        {
            
            RotateTowardsMouse();
        } 
        //else
        //{
            //RotateTowardsAnchor();
        //}
    }

    private bool IsHolding() {

        if(holding && !Input.GetMouseButton(1)) // Think we're holding right click but we aren't holding
        {
            holding = false;
            //Release();
            
        } else if(!holding && Input.GetMouseButton(1)) // Think we're not holding right click but we are holding
        {
            holding = true;
            StartHold();
            
        }
        return holding;
    }


    public void RotateTowardsMouse()
    {
        
        Vector2 mousePos = Input.mousePosition;

        Vector2 mouseDelta = mousePos - prevMousePos;
        prevMousePos = mousePos;

      
        float x = mouseDelta.x*Time.deltaTime * mouseRotateSpeed;
        float y = mouseDelta.y*Time.deltaTime * mouseRotateSpeed;
       

        RotateTowardAngles(x, y);

    }

   

    private void RotateTowardAngles(float x, float y)
    {
        
        transform.Rotate(Vector3.up, x);

        transform.RotateAround(transform.position, Vector3.right, y);
        
        

    }   

    private void StartHold()
    {
        //heldEuler = transform.eulerAngles;

        /*Vector2 normalizedMousePos = Input.mousePosition;
        normalizedMousePos.x /= Screen.width;
        normalizedMousePos.y /= Screen.height;

        normalizedMousePos -= Vector2.one * 0.5f;

        Vector3 initalPush = Vector3.zero;
        initalPush.x = normalizedMousePos.y;
        initalPush.y = normalizedMousePos.x;
        
        initalPush *= initMousePush;

        heldEuler += initalPush;*/
        prevMousePos = Input.mousePosition;


    }

    public void Release()
    {
        UpdateAnchor();
    }

    private void RotateTowardsAnchor()
    {
        //float x = Quaternion.Euler(anchor).

        //RotateTowardAngles(anchor);
    }

    private void UpdateAnchor()
    {
        Vector3 newAnchor = transform.eulerAngles;
        newAnchor /= 90;
        newAnchor.x = Mathf.Round(newAnchor.x);
        newAnchor.y = Mathf.Round(newAnchor.y);
        newAnchor.z = Mathf.Round(newAnchor.z);

        anchor = newAnchor * 90;


    }
}
