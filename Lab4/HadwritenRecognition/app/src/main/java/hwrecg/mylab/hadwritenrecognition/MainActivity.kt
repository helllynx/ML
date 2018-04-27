package hwrecg.mylab.hadwritenrecognition

import android.app.Activity
import android.content.Context
import android.graphics.*
import android.os.Bundle
import android.view.View
import android.widget.RelativeLayout
import android.widget.RelativeLayout.LayoutParams.*
import kotlinx.android.synthetic.main.activity_main.*
import android.graphics.Bitmap
import android.view.MotionEvent
import android.graphics.Bitmap.CompressFormat
import org.jetbrains.anko.doAsync
import java.io.*
import java.net.Socket
import android.util.Log
import java.nio.ByteBuffer
import java.nio.file.Files.size




class MainActivity : Activity() {

    var canvas: Canvas? = null
    var paint: Paint = Paint()
    var view: View? = null
    var path: Path = Path()
    var bitmap: Bitmap? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val pathToFile = getExternalFilesDir(null).absolutePath + "/image.png"

        view = SketchSheetView(this)

        releativeLayout.addView(view, RelativeLayout.LayoutParams(
                1200,
                1200))
        (view as SketchSheetView).isDrawingCacheEnabled = true
        paint.isDither = true
        paint.color = Color.parseColor("#000000")
        paint.style = Paint.Style.STROKE
        paint.strokeJoin = Paint.Join.ROUND
        paint.strokeCap = Paint.Cap.ROUND
        paint.strokeWidth = 120F

        val image = File(pathToFile)
        image.createNewFile()

        button_clear.setOnClickListener { path.reset()
            (view as SketchSheetView).destroyDrawingCache()}
        button_save.setOnClickListener {
            val b = (view as SketchSheetView).drawingCache
            val file = FileOutputStream(image)
            b.compress(CompressFormat.PNG, 100, file)

            sendFile(image, "10.0.2.124", 9090)
            (view as SketchSheetView).destroyDrawingCache()
        }

    }

    internal inner class SketchSheetView(context: Context) : View(context) {

        private val drawingClassArrayList = ArrayList<DrawingClass>()

        init {
            bitmap = Bitmap.createBitmap(1200, 1200, Bitmap.Config.ARGB_8888)
            canvas = Canvas(bitmap)
            this.setBackgroundColor(Color.WHITE)
        }

        override fun onTouchEvent(event: MotionEvent): Boolean {

            val pathWithPaint = DrawingClass()

            canvas?.drawPath(path, paint)

            if (event.action == MotionEvent.ACTION_DOWN) {
                path.moveTo(event.x, event.y)
                path.lineTo(event.x, event.y)
            } else if (event.action == MotionEvent.ACTION_MOVE) {
                path.lineTo(event.x, event.y)
                pathWithPaint.path = path
                pathWithPaint.paint = paint
                drawingClassArrayList.add(pathWithPaint)
            }

            invalidate()
            return true
        }

        override fun onDraw(canvas: Canvas) {
            super.onDraw(canvas)
            if (drawingClassArrayList.size > 0) {

                canvas.drawPath(
                        drawingClassArrayList[drawingClassArrayList.size - 1].path,
                        drawingClassArrayList[drawingClassArrayList.size - 1].paint)
            }
        }
    }

    inner class DrawingClass {

        var path: Path? = null
        var paint: Paint? = null
    }
//
//
//    fun sendFile(file: File, host: String, port: Int) {
//        doAsync {
//            try {
//                val s = Socket(host, port)
//
//                val dos = DataOutputStream(s.getOutputStream())
//                val fis = FileInputStream(file)
//                val buffer = ByteArray(4096)
//
//                while (fis.read(buffer) > 0) {
//                    dos.write(buffer)
//                }
//                fis.close()
//                dos.close()
//            } catch (e: Exception) {
//                e.printStackTrace()
//            }
//        }
//    }

    fun sendFile(file: File, host: String, port: Int) {
        doAsync {
            try {
                val socket = Socket(host, port)
                val outputStream = socket.getOutputStream()

                val fis = FileInputStream(file)

                val buffer = ByteArray(4096)
                val byteArrayOutputStream = ByteArrayOutputStream()

                while (fis.read(buffer) > 0) {
                    byteArrayOutputStream.write(buffer)
                }


                val size = ByteBuffer.allocate(4).putInt(byteArrayOutputStream.size()).array()
                outputStream.write(size)
                outputStream.write(byteArrayOutputStream.toByteArray())
                outputStream.flush()
                Log.d("IMAGE____","Flushed: " + System.currentTimeMillis())

                Thread.sleep(120000)
                Log.d("IMAGE____","Closing: " + System.currentTimeMillis())
                socket.close()
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
    }


    fun Long.longToBytes(): ByteArray {
        val buffer = ByteBuffer.allocate(java.lang.Long.BYTES)
        buffer.putLong(this)
        return buffer.array()
    }

    fun Int.toByteArray(): ByteArray {
        return byteArrayOf(this.ushr(24).toByte(), this.ushr(16).toByte(), this.ushr(8).toByte(), this.toByte())
    }

}



