using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DynamicBackground : MonoBehaviour
{

    [SerializeField] private BoardGameObj boardManager;
    [SerializeField] private Material backgroundMat;

    [SerializeField] private float updateSpeed;
    
    // Start is called before the first frame update
    void Start()
    {
        backgroundMat.SetFloat("_LerpVal", boardManager.GetCurrPlayer());
    }

    // Update is called once per frame
    void Update()
    {
        UpdateShaderVal("_LerpVal", boardManager.GetCurrPlayer(), updateSpeed);
    }


    private void UpdateShaderVal(string fieldName, float target, float speed)
    {
        float currVal = backgroundMat.GetFloat(fieldName);

        float newVal = Mathf.Lerp(currVal, target, Time.deltaTime * speed);



        backgroundMat.SetFloat(fieldName, newVal);

    }
}
